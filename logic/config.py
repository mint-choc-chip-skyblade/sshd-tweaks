from pathlib import Path
import yaml
from constants.configconstants import (
    CONFIG_FIELDS,
    ENTRANCE_TYPES,
    PREFERENCE_FIELDS,
    SETTING_ALIASES,
    get_default_setting,
)
from filepathconstants import PREFERENCES_PATH, WORDS_PATH

from .settings import *


class ConfigError(RuntimeError):
    pass


class Config:
    def __init__(self) -> None:
        self.seed: str = None  # type: ignore
        self.settings: list[SettingMap] = []
        self.num_worlds: int = 0
        self.output_dir: Path = None  # type: ignore
        self.font_family: str = None  # type: ignore
        self.font_size: int = 0
        self.verified_extract: bool = False


def create_default_config(filename: Path):
    config = load_preferences()

    for field in CONFIG_FIELDS:
        config.__setattr__(field, get_default_setting(field))

    config.settings.append(SettingMap())
    setting_map = config.settings[0]
    setting_map.other_mods = get_default_setting("other_mods")

    for setting_name in get_all_settings_info():
        setting_map.settings[setting_name] = create_default_setting(setting_name)

    write_config_to_file(filename, config)


def create_default_setting(setting_name: str) -> Setting:
    all_settings_info = get_all_settings_info()

    if (setting_info := all_settings_info.get(setting_name)) is None:
        raise ConfigError(f"Could not find setting info for setting: {setting_name}.")

    new_setting = Setting(
        setting_name,
        setting_info.options[setting_info.default_option_index],
        setting_info,
    )

    return new_setting


def write_config_to_file(
    filename: Path, config: Config, write_preferences: bool = True
):
    with open(filename, "w", encoding="utf-8") as config_file:
        config_out = {}

        for field in CONFIG_FIELDS:
            config_out[field] = config.__getattribute__(field)

        for i, setting_map in enumerate(config.settings):
            world_num = f"World {i + 1}"
            config_out[world_num] = {}

            for setting_name, setting in setting_map.settings.items():
                config_out[world_num][setting_name] = setting.value

            # Map other mods
            config_out[world_num]["other_mods"] = []

            for other_mod in setting_map.other_mods:
                config_out[world_num]["other_mods"].append(other_mod)

        yaml.safe_dump(config_out, config_file, sort_keys=False)

    if not write_preferences:
        return

    with open(PREFERENCES_PATH, "w", encoding="utf-8") as preferences_file:
        preferences_out = {}

        for field in PREFERENCE_FIELDS:
            preferences_out[field] = config.__getattribute__(field)

        # Make sure output_dir is always a string
        preferences_out["output_dir"] = preferences_out["output_dir"].as_posix()

        yaml.safe_dump(preferences_out, preferences_file, sort_keys=False)


def load_or_get_default_from_config(config: dict, setting_name: str):
    is_from_default = False

    if (setting_value := config.get(setting_name)) is None:
        setting_value = get_default_setting(setting_name)
        is_from_default = True

    return (setting_value, is_from_default)


def load_config_from_file(
    filepath: Path,
    config: Config | None = None,
    allow_rewrite: bool = True,
    create_if_blank: bool = False,
    default_on_invalid_value: bool = False,
) -> Config:
    if create_if_blank and not filepath.is_file():
        print("No config file found. Creating default config file.")
        create_default_config(filepath)

    config = load_preferences(config)

    # If the config is missing any options, set defaults and resave it afterwards
    rewrite_config: bool = False
    with open(filepath, encoding="utf-8") as config_file:
        config_in = yaml.safe_load(config_file)

        if config_in is None:
            config_in = dict()

        for field in CONFIG_FIELDS:
            field_value, is_from_default = load_or_get_default_from_config(
                config_in, field
            )
            config.__setattr__(field, field_value)

            if is_from_default:
                config_in[field] = field_value
                rewrite_config = True

        world_num = 1
        world_num_str = f"World {world_num}"

        # Create default World 1 if it doesn't exist already
        if world_num_str not in config_in:
            config_in[world_num_str] = {}

        # If config was passed into this function, clear the setting and start over
        config.settings.clear()

        settings_info = get_all_settings_info()
        while world_num_str in config_in:
            config.settings.append(SettingMap())
            cur_world_settings = config.settings[world_num - 1]

            # Loop through and parse all settings from the config
            # in the order of the settings info
            for setting_name, info in settings_info.items():

                # If a setting does not exist, check old aliases
                # or create a new entry for the setting
                if setting_name not in config_in[world_num_str]:
                    rewrite_config = True
                    if old_setting_alias := SETTING_ALIASES.get(setting_name, False):
                        if old_alias_value := config_in[world_num_str].get(
                            old_setting_alias, False
                        ):
                            cur_world_settings.settings[setting_name] = Setting(
                                setting_name, old_alias_value, info
                            )
                            continue
                    default_value = info.options[info.default_option_index]
                    cur_world_settings.settings[setting_name] = Setting(
                        setting_name, default_value, info
                    )
                # Otherwise read in the setting normally
                else:
                    setting_value = config_in[world_num_str][setting_name]

                    if setting_value not in settings_info[setting_name].options:
                        if default_on_invalid_value:
                            rewrite_config = True
                            default_value = info.options[info.default_option_index]
                            print(
                                f'"{setting_value}" is not a valid value for setting "{setting_name}". Defaulting to "{default_value}"'
                            )
                            setting_value = default_value
                        else:
                            raise ConfigError(
                                f'"{setting_value}" is not a valid value for setting "{setting_name}"'
                            )

                    cur_world_settings.settings[setting_name] = Setting(
                        setting_name, setting_value, settings_info[setting_name]
                    )
                # TODO: Hex codes

            # Special handling for other settings
            for setting_name in ("other_mods",):
                if config_in[world_num_str].get(setting_name) is None:
                    cur_world_settings.__setattr__(
                        setting_name, get_default_setting(setting_name)
                    )
                    rewrite_config = True

                elif setting_name == "other_mods":
                    other_mods = config_in[world_num_str][setting_name]

                    if not isinstance(other_mods, list):
                        raise ConfigError(
                            f"Could not read value for setting '{setting_name}'. Are you sure that {setting_name} is defined as a list? Current value: {other_mods}."
                        )

                    cur_world_settings.other_mods = other_mods

            world_num += 1
            world_num_str = f"World {world_num}"

    if rewrite_config and allow_rewrite:
        write_config_to_file(filepath, config)

    return config


def load_preferences(config: Config | None = None) -> Config:
    if config is None:
        config = Config()

    filepath = Path(PREFERENCES_PATH)

    if not filepath.is_file():
        with open(filepath, "w", encoding="utf-8") as _:
            pass

    # If missing any options, set defaults and resave it afterwards
    rewrite_preferences: bool = False
    with open(filepath, "r", encoding="utf-8") as preferences_file:
        preferences_in = yaml.safe_load(preferences_file)

        if preferences_in is None:
            preferences_in = dict()

        for field in PREFERENCE_FIELDS:
            field_value, is_from_default = load_or_get_default_from_config(
                preferences_in, field
            )
            config.__setattr__(field, field_value)

            if is_from_default:
                preferences_in[field] = field_value
                rewrite_preferences = True

        # Make sure output_dir is always a Path object in config...
        config.output_dir = Path(config.output_dir)
        # ...and a string if being dumped
        preferences_in["output_dir"] = Path(preferences_in["output_dir"]).as_posix()

    if rewrite_preferences:
        with open(filepath, "w", encoding="utf-8") as preferences_file:
            yaml.safe_dump(preferences_in, preferences_file, sort_keys=False)

    return config
