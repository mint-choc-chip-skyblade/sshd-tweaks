import json
import qdarktheme

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import (
    QAbstractButton,
    QComboBox,
    QFontComboBox,
    QSpinBox,
)
from constants.configconstants import DEFAULT_SETTINGS

from filepathconstants import (
    CONFIG_PATH,
    DYSLEXIC_FONT_PATH,
    FONT_PATH,
)
from logic.config import Config, write_config_to_file

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gui.main import Main
    from gui.ui.ui_main import Ui_main_window

# Add stylesheet overrides here.
BASE_STYLE_SHEET_OVERRIDES = ""

THEME_MODE_OPTIONS = ("Light", "Dark", "Auto")
THEME_PRESETS_OPTIONS = ("Default", "High Contrast", "Readability")


class Accessibility:
    def __init__(self, main: "Main", ui: "Ui_main_window"):
        self.main = main
        self.ui = ui
        self.config: Config = main.config

        QFontDatabase.addApplicationFont(FONT_PATH.as_posix())
        QFontDatabase.addApplicationFont(DYSLEXIC_FONT_PATH.as_posix())

        self.ui.font_reset_button.clicked.connect(self.reset_font)

        font_family_widget: QFontComboBox = getattr(self.ui, "font_family_combo_box")
        font_family_widget.setCurrentIndex(
            font_family_widget.findText(self.config.font_family)
        )
        font_family_widget.currentFontChanged.connect(self.update_font)

        font_size_widget: QSpinBox = getattr(self.ui, "font_size_spin_box")
        font_size_widget.valueChanged.connect(self.update_font)
        font_size_widget.setValue(self.config.font_size)

        self.update_font()

    def update_font(self):
        font_family_widget: QFontComboBox = getattr(self.ui, "font_family_combo_box")
        self.config.font_family = font_family_widget.currentText()

        font_size_widget: QSpinBox = getattr(self.ui, "font_size_spin_box")
        self.config.font_size = font_size_widget.value()

        write_config_to_file(CONFIG_PATH, self.config)

        self.main.setStyleSheet(
            BASE_STYLE_SHEET_OVERRIDES
            + f"QWidget {{ font-family: { self.config.font_family }; font-size: { self.config.font_size }pt }}"
        )

    def reset_font(self):
        font_index = self.ui.font_family_combo_box.findText(
            DEFAULT_SETTINGS["font_family"]
        )
        self.ui.font_family_combo_box.setCurrentIndex(font_index)
        self.ui.font_size_spin_box.setValue(10)
