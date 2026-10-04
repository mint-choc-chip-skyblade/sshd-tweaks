from collections import Counter
from functools import partial

from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QLineEdit,
    QMessageBox,
    QSpinBox,
    QWidget,
    QAbstractButton,
    QInputDialog,
    QSpacerItem,
    QSizePolicy,
)

import pyclip

from constants.configconstants import (
    LOCATION_ALIASES,
    get_default_setting,
    get_new_seed,
)
from constants.guiconstants import *
from filepathconstants import (
    COMBINED_MODS_FOLDER,
    CONFIG_PATH,
    OTHER_MODS_PATH,
)
from gui.components.list_pair import ListPair
from gui.components.tristate_check_box import RandoTriStateCheckBox
from logic.config import Config, load_config_from_file, write_config_to_file
from logic.settings import Setting
from sslib.yaml import yaml_load

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gui.main import Main
    from gui.ui.ui_main import Ui_main_window


class Settings:
    def __init__(self, main: "Main", ui: "Ui_main_window"):
        self.main = main
        self.ui = ui
        self.config: Config = main.config

        self.settings = self.config.settings[0].settings

        self.set_setting_descriptions(None)
        self.ui.reset_settings_to_default_button.clicked.connect(self.reset)

        # Init other settings
        for setting_name, setting_info in self.settings.items():
            current_option_value = setting_info.value

            widget = None  # type: ignore
            label = None  # type: ignore

            try:
                widget: QWidget = getattr(self.ui, "setting_" + setting_name)
            except:
                print(f"Could not find widget for setting: {setting_name}.")
                continue

            # Used to change the settings description when mousing over a setting
            widget.installEventFilter(self.main)

            try:
                label = getattr(self.ui, setting_name + "_label")
                label.setText(setting_info.info.pretty_name)
                label.installEventFilter(self.main)
            except:
                pass

            if isinstance(widget, RandoTriStateCheckBox):
                if current_option_value == "on":
                    widget.setChecked(True)
                elif current_option_value == "random":
                    widget.setCheckState(Qt.CheckState.PartiallyChecked)
                elif current_option_value == "off":
                    widget.setChecked(False)
                else:
                    raise TypeError(
                        f"Setting '{setting_name}' has value '{current_option_value}' which is invalid for a QAbstractButton. Expected either 'on' or 'off'."
                    )

                widget.setText(setting_info.info.pretty_name)
                widget.clicked.connect(partial(self.update_from_gui, widget))
            elif isinstance(widget, QCheckBox):
                raise Exception(
                    f"All settings mapped to QCheckBox objects need promoting to RandoTriStateCheckBox objects in the Qt Designer. Fix widget with name: {widget.objectName()}."
                )
            elif isinstance(widget, QComboBox):  # pick one option
                for option in setting_info.info.pretty_options:
                    widget.addItem(option)

                widget.setCurrentIndex(
                    setting_info.info.options.index(setting_info.value)
                )
                widget.currentIndexChanged.connect(
                    partial(self.update_from_gui, widget)
                )
            elif isinstance(widget, QSpinBox):  # pick a value
                widget.setMinimum(
                    int(setting_info.info.options[0]) - 1
                )  # -1 for special value
                widget.setMaximum(int(setting_info.info.options[-2]))
                widget.setSpecialValueText("Random")

                if current_option_value == "random":
                    widget.setValue(widget.minimum())
                else:
                    widget.setValue(int(current_option_value))

                widget.valueChanged.connect(partial(self.update_from_gui, widget))

        # Force descriptions to update before changing any setting
        self.update_from_gui()

    def update_from_gui(
        self,
        from_widget=None,
        widget_info=None,
        update_descriptions: bool = True,
        allow_rewrite: bool = True,
    ):
        for setting_name, setting in self.settings.items():
            widget = None  # type: ignore

            try:
                widget: QWidget = getattr(self.ui, "setting_" + setting_name)
            except:
                # print(f"Cannot find attribute for '{setting_name}', ignoring.")
                continue

            if not widget:
                continue

            new_setting = setting
            new_option = ""

            if isinstance(widget, RandoTriStateCheckBox):
                if widget.checkState() == Qt.CheckState.Checked:
                    new_option = "on"
                elif widget.checkState() == Qt.CheckState.PartiallyChecked:
                    new_option = "random"

                    if not self.config.tutorial_random_settings and from_widget:
                        self.main.fi_info_dialog.show_dialog(
                            "Random Setting Information",
                            f"Checkboxes have 3 states: off, on, and 'random'. Checkboxes that have a dash (-) instead of a tick mean that the randomizer will randomly pick if that setting is on or off when you click 'Randomize'.<br><br>You can middle-click any setting to quickly reset it back to its default or right-click to view a description of the possible options for a setting.",
                        )
                        self.config.tutorial_random_settings = True
                else:
                    new_option = "off"
            elif isinstance(widget, QComboBox):
                new_option = new_setting.info.options[widget.currentIndex()]
            elif isinstance(widget, QSpinBox):
                new_option = str(widget.value())

            self.settings[setting_name] = self.get_updated_setting(
                new_setting, new_option
            )

            widget.setToolTip(
                "➜ Right-click to view all options.\n➜ Middle-click to reset to default."
            )

        self.config.settings[0].settings = self.settings

        self.generate_other_mods_list()

        if allow_rewrite:
            write_config_to_file(CONFIG_PATH, self.config)

        if update_descriptions:
            self.update_descriptions(from_widget)

    def update_from_config(self):
        # Update other settings
        for setting_name, setting_info in self.settings.items():
            current_option_value = setting_info.value

            widget = None  # type: ignore
            label = None  # type: ignore

            try:
                widget: QWidget = getattr(self.ui, "setting_" + setting_name)
            except:
                print(f"Could not find widget for setting: {setting_name}.")
                continue

            widget.blockSignals(True)

            try:
                label = getattr(self.ui, setting_name + "_label")
                label.setText(setting_info.info.pretty_name)
            except:
                pass

            if isinstance(widget, QCheckBox):
                if current_option_value == "on":
                    widget.setChecked(True)
                elif current_option_value == "random":
                    widget.setCheckState(Qt.CheckState.PartiallyChecked)
                elif current_option_value == "off":
                    widget.setChecked(False)
                else:
                    raise TypeError(
                        f"Setting '{setting_name}' has value '{current_option_value}' which is invalid for a QAbstractButton. Expected either 'on' or 'off'."
                    )

                widget.setText(setting_info.info.pretty_name)
            elif isinstance(widget, QComboBox):  # pick one option
                widget.setCurrentIndex(
                    setting_info.info.options.index(setting_info.value)
                )
            elif isinstance(widget, QSpinBox):  # pick a value
                if current_option_value == "random":
                    widget.setValue(widget.minimum())
                else:
                    widget.setValue(int(current_option_value))

            widget.blockSignals(False)

        # Verifies all the settings and forces a config rewrite
        self.update_from_gui()

    def get_updated_setting(self, setting: Setting, value: str) -> Setting:
        if value == "":
            raise ValueError(
                f"Cannot update setting '{setting.name}' value as value is empty."
            )

        new_setting = setting

        if ((value.startswith("-") and value[1:].isdigit()) or value.isdigit()) and int(
            value
        ) == int(setting.info.options[0]) - 1:
            option_index = setting.info.options.index("random")
            new_setting.value = "random"
        else:
            option_index = setting.info.options.index(value)
            new_setting.value = value

        new_setting.update_current_value(option_index)

        return new_setting

    def reset_single(
        self, setting: Setting | None, from_reset_all: bool = False
    ) -> bool:
        if setting is None:
            return False

        setting_name = setting.info.name
        widget = None  # type: ignore

        try:
            widget: QWidget = getattr(self.ui, "setting_" + setting_name)
        except:
            # print(f"Cannot find attribute for '{setting_name}', ignoring.")
            return False

        if not widget:
            return False

        default_option = setting.info.options[setting.info.default_option_index]

        if isinstance(widget, QCheckBox):
            if default_option == "on":
                widget.setCheckState(Qt.CheckState.Checked)
            elif default_option == "random":
                widget.setCheckState(Qt.CheckState.PartiallyChecked)
            elif default_option == "off":
                widget.setCheckState(Qt.CheckState.Unchecked)
        elif isinstance(widget, QComboBox):
            widget.setCurrentIndex(setting.info.default_option_index)
        elif isinstance(widget, QSpinBox):
            widget.setValue(int(default_option))

        # Otherwise, the config file is re-written once for *every* setting
        if not from_reset_all:
            self.update_from_gui(from_widget=widget, update_descriptions=False)

        return True

    def reset(self):
        confirm_choice = self.main.fi_question_dialog.show_dialog(
            "Are you sure?",
            "Are you sure you want to reset EVERY option?",
        )

        if confirm_choice != QMessageBox.StandardButton.Yes:
            return

        for setting_name, setting in self.settings.items():
            self.reset_single(setting, from_reset_all=True)

    def get_setting_from_widget(self, widget: QObject | None) -> Setting | None:
        if not widget:
            return None

        widget_name = widget.objectName()
        setting_name = widget_name.removeprefix("setting_")
        setting_name = setting_name.removesuffix("_label")

        if self.settings.get(setting_name):
            return self.settings[setting_name]
        else:
            return None

    def set_setting_descriptions(self, setting: Setting | None):
        if setting is None:
            default_description = (
                OPTION_PREFIX
                + "Hover over a setting to see a description of the current and default options.<br>"
            )
            default_description += (
                OPTION_PREFIX
                + "Right click a setting to see a full description of all the options.<br>"
            )
            default_description += (
                OPTION_PREFIX + "Middle click a setting to reset it to default."
            )

            self.ui.settings_current_option_description_label.setText(
                default_description
            )
            self.ui.settings_default_option_description_label.setText("")
        else:
            current_option_description = (
                "<b>Current Option</b> (<i>Right-click to see all the options</i>):<br>"
            )
            current_option_description += self.format_description(
                setting, setting.current_option_index
            )
            default_option_description = "<b>Default Option</b>:<br>"
            default_option_description += self.format_description(
                setting, setting.info.default_option_index
            )

            self.ui.settings_current_option_description_label.setText(
                current_option_description
            )
            self.ui.settings_default_option_description_label.setText(
                default_option_description
            )

    def format_description(
        self, setting: Setting, option_index: int, custom_option_name: str | None = None
    ) -> str:
        formatted_description = "<b>" + OPTION_PREFIX

        if custom_option_name:
            formatted_description += custom_option_name + "</b>: "
        else:
            formatted_description += (
                setting.info.pretty_options[option_index] + "</b>: "
            )

        formatted_description += setting.info.descriptions[option_index]
        return formatted_description

    def update_descriptions(self, target: QObject | None) -> bool:
        if setting := self.get_setting_from_widget(target):
            self.set_setting_descriptions(setting)
        else:
            self.set_setting_descriptions(None)

        return True

    def show_full_descriptions(self, target: QWidget | None) -> bool:
        if target is None or not (setting := self.get_setting_from_widget(target)):
            return True

        description_text = "<b>Current Option</b>:<br>"
        description_text += self.format_description(
            setting, setting.current_option_index
        )
        description_text += "<br><br><b>Default Option</b>:<br>"
        description_text += self.format_description(
            setting, setting.info.default_option_index
        )
        description_text += "<br><br><b>All Options</b>:<br>"

        try:
            widget: QWidget = getattr(self.ui, "setting_" + setting.name)
        except:
            raise Exception(f"Could not find widget for setting: {setting.name}.")

        if isinstance(widget, QSpinBox):
            last_index = len(setting.info.options) - 1

            if is_random := setting.info.options[last_index] == "random":
                last_index -= 1

            description_text += self.format_description(
                setting,
                0,
                custom_option_name=f"{setting.info.options[0]}-{setting.info.options[last_index]}",
            )

            if is_random:
                description_text += "<br>" + self.format_description(setting, -1)
        else:
            for option_index in range(0, len(setting.info.options)):
                description_text += (
                    self.format_description(setting, option_index) + "<br>"
                )

        dialog_title = setting.info.pretty_name + " Options"
        self.main.fi_info_dialog.show_dialog(title=dialog_title, text=description_text)
        return True

    def generate_other_mods_list(self):
        self.main.clear_layout(self.ui.other_mods_scroll_layout)

        other_mods_paths = list(OTHER_MODS_PATH.glob("*"))
        other_mods_paths.sort()
        found_mods = []

        for mod_path in other_mods_paths:
            if mod_path.is_dir():
                mod_name = mod_path.name

                # Don't include the combined mods folder as a mod folder. Normally this folder is deleted, but
                # if generation fails for some reason, then it might not get deleted.
                if mod_name == COMBINED_MODS_FOLDER:
                    continue

                # Don't include the mod if it has an exefs folder. We don't support integrating other mods which modify code
                if (OTHER_MODS_PATH / mod_name / "exefs").exists():
                    continue

                mod_checkbox = QCheckBox(mod_name)
                mod_checkbox.clicked.connect(self.update_mods_in_config)
                if mod_name in self.config.settings[0].other_mods:
                    mod_checkbox.setChecked(True)
                    found_mods.append(mod_name)

                self.ui.other_mods_scroll_layout.addWidget(mod_checkbox)

        # Add a vertical spacer to push the mod list up
        self.ui.other_mods_scroll_layout.addSpacerItem(
            QSpacerItem(
                20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )
        )

        # Remove mods from config which weren't found
        for mod_name in self.config.settings[0].other_mods.copy():
            if mod_name not in found_mods:
                print(
                    f"Removing mod {mod_name} from other_mods list as the QCheckbox for the mod could not be found"
                )
                self.config.settings[0].other_mods.remove(mod_name)

    def update_mods_in_config(self):
        other_mods = self.config.settings[0].other_mods
        other_mods.clear()
        for checkbox in self.ui.other_mods_scroll_widget.findChildren(QCheckBox):
            if checkbox.isChecked():
                other_mods.append(checkbox.text())

        self.update_from_gui()
