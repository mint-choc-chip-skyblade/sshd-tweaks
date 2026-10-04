from filepathconstants import DEFAULT_OUTPUT_PATH
from .world import World
from .config import *
from .settings import *
from util.text import load_text_data

from gui.dialogs.dialog_header import print_progress_text, update_progress_value
import time
import random


def generate(config_file: Path) -> World:
    start_load_config_time = time.process_time()
    get_all_settings_info()
    load_text_data()

    config = load_config_from_file(config_file, create_if_blank=True)

    if config.output_dir != DEFAULT_OUTPUT_PATH and (
        not config.output_dir.exists() or not config.output_dir.is_dir()
    ):
        raise ConfigError(f"""
The output folder you have specified cannot be found ({config.output_dir.as_posix()}).
Please choose a valid folder and try again.""")

    print(
        f"Loading config took {(time.process_time() - start_load_config_time)} seconds"
    )

    update_progress_value(7)

    return generate_patcher(config)


def generate_patcher(config: Config) -> World:
    update_progress_value(8)

    worlds: list[World] = []
    world = World(0)

    print_progress_text(f"Building world")
    setting_map = config.settings[0]
    world.setting_map = setting_map
    world.resolve_conflicting_settings()
    world.config = config

    return world
