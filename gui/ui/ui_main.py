# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFontComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

from gui.components.tristate_check_box import RandoTriStateCheckBox

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(900, 800)
        main_window.setStyleSheet(u"QToolTip {color: #000000; background-color: #FFFFFF;}")
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"QToolTip {color: #000000; background-color: #FFFFFF;}")
        self.verticalLayout_2 = QVBoxLayout(self.central_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setObjectName(u"tab_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_widget.setStyleSheet(u"QToolTip {color: #000000; background-color: #FFFFFF;}")
        self.tab_widget.setTabShape(QTabWidget.TabShape.Rounded)
        self.getting_started_tab = QWidget()
        self.getting_started_tab.setObjectName(u"getting_started_tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.getting_started_tab.sizePolicy().hasHeightForWidth())
        self.getting_started_tab.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.getting_started_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.how_to_group_box = QGroupBox(self.getting_started_tab)
        self.how_to_group_box.setObjectName(u"how_to_group_box")
        sizePolicy.setHeightForWidth(self.how_to_group_box.sizePolicy().hasHeightForWidth())
        self.how_to_group_box.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.how_to_group_box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, -1, -1)
        self.how_to_extract_label = QLabel(self.how_to_group_box)
        self.how_to_extract_label.setObjectName(u"how_to_extract_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.how_to_extract_label.sizePolicy().hasHeightForWidth())
        self.how_to_extract_label.setSizePolicy(sizePolicy2)
        self.how_to_extract_label.setTextFormat(Qt.TextFormat.RichText)
        self.how_to_extract_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.how_to_extract_label.setWordWrap(True)
        self.how_to_extract_label.setOpenExternalLinks(True)
        self.how_to_extract_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_11.addWidget(self.how_to_extract_label)

        self.line = QFrame(self.how_to_group_box)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line)

        self.choose_settings_label = QLabel(self.how_to_group_box)
        self.choose_settings_label.setObjectName(u"choose_settings_label")
        sizePolicy2.setHeightForWidth(self.choose_settings_label.sizePolicy().hasHeightForWidth())
        self.choose_settings_label.setSizePolicy(sizePolicy2)
        self.choose_settings_label.setTextFormat(Qt.TextFormat.RichText)
        self.choose_settings_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.choose_settings_label.setWordWrap(True)
        self.choose_settings_label.setOpenExternalLinks(True)
        self.choose_settings_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_11.addWidget(self.choose_settings_label)

        self.line_2 = QFrame(self.how_to_group_box)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_2)

        self.how_to_generate_label = QLabel(self.how_to_group_box)
        self.how_to_generate_label.setObjectName(u"how_to_generate_label")
        sizePolicy2.setHeightForWidth(self.how_to_generate_label.sizePolicy().hasHeightForWidth())
        self.how_to_generate_label.setSizePolicy(sizePolicy2)
        self.how_to_generate_label.setTextFormat(Qt.TextFormat.RichText)
        self.how_to_generate_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.how_to_generate_label.setWordWrap(True)
        self.how_to_generate_label.setOpenExternalLinks(True)
        self.how_to_generate_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_11.addWidget(self.how_to_generate_label)

        self.line_3 = QFrame(self.how_to_group_box)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_3)

        self.how_to_running_label = QLabel(self.how_to_group_box)
        self.how_to_running_label.setObjectName(u"how_to_running_label")
        sizePolicy2.setHeightForWidth(self.how_to_running_label.sizePolicy().hasHeightForWidth())
        self.how_to_running_label.setSizePolicy(sizePolicy2)
        self.how_to_running_label.setTextFormat(Qt.TextFormat.RichText)
        self.how_to_running_label.setScaledContents(False)
        self.how_to_running_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.how_to_running_label.setWordWrap(True)
        self.how_to_running_label.setOpenExternalLinks(True)
        self.how_to_running_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_11.addWidget(self.how_to_running_label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)


        self.verticalLayout_4.addWidget(self.how_to_group_box)

        self.middle_grid_layout = QGridLayout()
        self.middle_grid_layout.setObjectName(u"middle_grid_layout")
        self.middle_grid_layout.setContentsMargins(-1, -1, -1, 0)
        self.useful_info_group_box = QGroupBox(self.getting_started_tab)
        self.useful_info_group_box.setObjectName(u"useful_info_group_box")
        sizePolicy.setHeightForWidth(self.useful_info_group_box.sizePolicy().hasHeightForWidth())
        self.useful_info_group_box.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.useful_info_group_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.guides_label = QLabel(self.useful_info_group_box)
        self.guides_label.setObjectName(u"guides_label")
        sizePolicy.setHeightForWidth(self.guides_label.sizePolicy().hasHeightForWidth())
        self.guides_label.setSizePolicy(sizePolicy)
        self.guides_label.setTextFormat(Qt.TextFormat.RichText)
        self.guides_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.guides_label.setWordWrap(True)
        self.guides_label.setOpenExternalLinks(True)
        self.guides_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.guides_label)

        self.community_label = QLabel(self.useful_info_group_box)
        self.community_label.setObjectName(u"community_label")
        sizePolicy.setHeightForWidth(self.community_label.sizePolicy().hasHeightForWidth())
        self.community_label.setSizePolicy(sizePolicy)
        self.community_label.setTextFormat(Qt.TextFormat.RichText)
        self.community_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.community_label.setWordWrap(True)
        self.community_label.setOpenExternalLinks(True)
        self.community_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.community_label)


        self.middle_grid_layout.addWidget(self.useful_info_group_box, 0, 0, 1, 1)

        self.accessibility_group_box = QGroupBox(self.getting_started_tab)
        self.accessibility_group_box.setObjectName(u"accessibility_group_box")
        sizePolicy.setHeightForWidth(self.accessibility_group_box.sizePolicy().hasHeightForWidth())
        self.accessibility_group_box.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.accessibility_group_box)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.theming_fonts = QGroupBox(self.accessibility_group_box)
        self.theming_fonts.setObjectName(u"theming_fonts")
        self.verticalLayout_12 = QVBoxLayout(self.theming_fonts)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.font_family_layout = QHBoxLayout()
        self.font_family_layout.setObjectName(u"font_family_layout")
        self.font_family_label = QLabel(self.theming_fonts)
        self.font_family_label.setObjectName(u"font_family_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.font_family_label.sizePolicy().hasHeightForWidth())
        self.font_family_label.setSizePolicy(sizePolicy3)

        self.font_family_layout.addWidget(self.font_family_label)

        self.font_family_combo_box = QFontComboBox(self.theming_fonts)
        self.font_family_combo_box.setObjectName(u"font_family_combo_box")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.font_family_combo_box.sizePolicy().hasHeightForWidth())
        self.font_family_combo_box.setSizePolicy(sizePolicy4)
        self.font_family_combo_box.setEditable(False)
        self.font_family_combo_box.setMinimumContentsLength(1)
        self.font_family_combo_box.setFontFilters(QFontComboBox.FontFilter.ScalableFonts)
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(10)
        self.font_family_combo_box.setCurrentFont(font)

        self.font_family_layout.addWidget(self.font_family_combo_box)


        self.verticalLayout_12.addLayout(self.font_family_layout)

        self.font_size_layout = QHBoxLayout()
        self.font_size_layout.setObjectName(u"font_size_layout")
        self.font_size_label = QLabel(self.theming_fonts)
        self.font_size_label.setObjectName(u"font_size_label")

        self.font_size_layout.addWidget(self.font_size_label)

        self.font_size_spin_box = QSpinBox(self.theming_fonts)
        self.font_size_spin_box.setObjectName(u"font_size_spin_box")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.font_size_spin_box.sizePolicy().hasHeightForWidth())
        self.font_size_spin_box.setSizePolicy(sizePolicy5)
        self.font_size_spin_box.setMinimum(6)
        self.font_size_spin_box.setMaximum(14)
        self.font_size_spin_box.setValue(10)

        self.font_size_layout.addWidget(self.font_size_spin_box)


        self.verticalLayout_12.addLayout(self.font_size_layout)

        self.font_reset_button = QPushButton(self.theming_fonts)
        self.font_reset_button.setObjectName(u"font_reset_button")

        self.verticalLayout_12.addWidget(self.font_reset_button)

        self.fonts_vspacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.fonts_vspacer)


        self.horizontalLayout_6.addWidget(self.theming_fonts)

        self.horizontalLayout_6.setStretch(0, 1)

        self.middle_grid_layout.addWidget(self.accessibility_group_box, 0, 1, 1, 1)

        self.middle_grid_layout.setColumnStretch(0, 1)
        self.middle_grid_layout.setColumnStretch(1, 1)

        self.verticalLayout_4.addLayout(self.middle_grid_layout)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        self.tab_widget.addTab(self.getting_started_tab, "")
        self.tweaks_tab = QWidget()
        self.tweaks_tab.setObjectName(u"tweaks_tab")
        sizePolicy1.setHeightForWidth(self.tweaks_tab.sizePolicy().hasHeightForWidth())
        self.tweaks_tab.setSizePolicy(sizePolicy1)
        self.gridLayout_9 = QGridLayout(self.tweaks_tab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.dungeons_group_box = QGroupBox(self.tweaks_tab)
        self.dungeons_group_box.setObjectName(u"dungeons_group_box")
        self.verticalLayout_16 = QVBoxLayout(self.dungeons_group_box)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.boss_key_puzzles_label = QLabel(self.dungeons_group_box)
        self.boss_key_puzzles_label.setObjectName(u"boss_key_puzzles_label")

        self.verticalLayout_16.addWidget(self.boss_key_puzzles_label)

        self.setting_boss_key_puzzles = QComboBox(self.dungeons_group_box)
        self.setting_boss_key_puzzles.setObjectName(u"setting_boss_key_puzzles")

        self.verticalLayout_16.addWidget(self.setting_boss_key_puzzles)

        self.setting_spawn_hearts = RandoTriStateCheckBox(self.dungeons_group_box)
        self.setting_spawn_hearts.setObjectName(u"setting_spawn_hearts")

        self.verticalLayout_16.addWidget(self.setting_spawn_hearts)

        self.setting_upgraded_skyward_strike = RandoTriStateCheckBox(self.dungeons_group_box)
        self.setting_upgraded_skyward_strike.setObjectName(u"setting_upgraded_skyward_strike")

        self.verticalLayout_16.addWidget(self.setting_upgraded_skyward_strike)

        self.setting_faster_air_meter_depletion = RandoTriStateCheckBox(self.dungeons_group_box)
        self.setting_faster_air_meter_depletion.setObjectName(u"setting_faster_air_meter_depletion")

        self.verticalLayout_16.addWidget(self.setting_faster_air_meter_depletion)

        self.damage_multiplier_layout = QHBoxLayout()
        self.damage_multiplier_layout.setObjectName(u"damage_multiplier_layout")
        self.damage_multiplier_label = QLabel(self.dungeons_group_box)
        self.damage_multiplier_label.setObjectName(u"damage_multiplier_label")

        self.damage_multiplier_layout.addWidget(self.damage_multiplier_label)

        self.setting_damage_multiplier = QSpinBox(self.dungeons_group_box)
        self.setting_damage_multiplier.setObjectName(u"setting_damage_multiplier")
        sizePolicy5.setHeightForWidth(self.setting_damage_multiplier.sizePolicy().hasHeightForWidth())
        self.setting_damage_multiplier.setSizePolicy(sizePolicy5)

        self.damage_multiplier_layout.addWidget(self.setting_damage_multiplier)


        self.verticalLayout_16.addLayout(self.damage_multiplier_layout)

        self.ammo_availability_label = QLabel(self.dungeons_group_box)
        self.ammo_availability_label.setObjectName(u"ammo_availability_label")

        self.verticalLayout_16.addWidget(self.ammo_availability_label)

        self.setting_ammo_availability = QComboBox(self.dungeons_group_box)
        self.setting_ammo_availability.setObjectName(u"setting_ammo_availability")

        self.verticalLayout_16.addWidget(self.setting_ammo_availability)

        self.minigame_difficulty_label = QLabel(self.dungeons_group_box)
        self.minigame_difficulty_label.setObjectName(u"minigame_difficulty_label")

        self.verticalLayout_16.addWidget(self.minigame_difficulty_label)

        self.setting_minigame_difficulty = QComboBox(self.dungeons_group_box)
        self.setting_minigame_difficulty.setObjectName(u"setting_minigame_difficulty")

        self.verticalLayout_16.addWidget(self.setting_minigame_difficulty)

        self.random_trial_object_positions_label = QLabel(self.dungeons_group_box)
        self.random_trial_object_positions_label.setObjectName(u"random_trial_object_positions_label")

        self.verticalLayout_16.addWidget(self.random_trial_object_positions_label)

        self.setting_random_trial_object_positions = QComboBox(self.dungeons_group_box)
        self.setting_random_trial_object_positions.setObjectName(u"setting_random_trial_object_positions")

        self.verticalLayout_16.addWidget(self.setting_random_trial_object_positions)


        self.gridLayout_9.addWidget(self.dungeons_group_box, 0, 0, 1, 1)

        self.dungeons_vspacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.dungeons_vspacer, 2, 0, 1, 1)

        self.other_settings_group_box = QGroupBox(self.tweaks_tab)
        self.other_settings_group_box.setObjectName(u"other_settings_group_box")
        sizePolicy.setHeightForWidth(self.other_settings_group_box.sizePolicy().hasHeightForWidth())
        self.other_settings_group_box.setSizePolicy(sizePolicy)
        self.verticalLayout_32 = QVBoxLayout(self.other_settings_group_box)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.setting_enable_back_in_time = RandoTriStateCheckBox(self.other_settings_group_box)
        self.setting_enable_back_in_time.setObjectName(u"setting_enable_back_in_time")

        self.verticalLayout_32.addWidget(self.setting_enable_back_in_time)

        self.setting_allow_flying_at_night = RandoTriStateCheckBox(self.other_settings_group_box)
        self.setting_allow_flying_at_night.setObjectName(u"setting_allow_flying_at_night")

        self.verticalLayout_32.addWidget(self.setting_allow_flying_at_night)


        self.gridLayout_9.addWidget(self.other_settings_group_box, 1, 0, 1, 1)

        self.gridLayout_9.setColumnStretch(0, 1)
        self.tab_widget.addTab(self.tweaks_tab, "")
        self.cosmetics_tab = QWidget()
        self.cosmetics_tab.setObjectName(u"cosmetics_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.cosmetics_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.player_cosmetics_group_box = QGroupBox(self.cosmetics_tab)
        self.player_cosmetics_group_box.setObjectName(u"player_cosmetics_group_box")
        self.verticalLayout_37 = QVBoxLayout(self.player_cosmetics_group_box)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.setting_tunic_swap = RandoTriStateCheckBox(self.player_cosmetics_group_box)
        self.setting_tunic_swap.setObjectName(u"setting_tunic_swap")

        self.verticalLayout_37.addWidget(self.setting_tunic_swap)

        self.setting_lightning_skyward_strike = RandoTriStateCheckBox(self.player_cosmetics_group_box)
        self.setting_lightning_skyward_strike.setObjectName(u"setting_lightning_skyward_strike")

        self.verticalLayout_37.addWidget(self.setting_lightning_skyward_strike)


        self.verticalLayout_10.addWidget(self.player_cosmetics_group_box)

        self.audio_cosmetics_group_box = QGroupBox(self.cosmetics_tab)
        self.audio_cosmetics_group_box.setObjectName(u"audio_cosmetics_group_box")
        self.verticalLayout_35 = QVBoxLayout(self.audio_cosmetics_group_box)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.randomize_music_label = QLabel(self.audio_cosmetics_group_box)
        self.randomize_music_label.setObjectName(u"randomize_music_label")

        self.verticalLayout_35.addWidget(self.randomize_music_label)

        self.setting_randomize_music = QComboBox(self.audio_cosmetics_group_box)
        self.setting_randomize_music.setObjectName(u"setting_randomize_music")

        self.verticalLayout_35.addWidget(self.setting_randomize_music)

        self.setting_cutoff_game_over_music = RandoTriStateCheckBox(self.audio_cosmetics_group_box)
        self.setting_cutoff_game_over_music.setObjectName(u"setting_cutoff_game_over_music")

        self.verticalLayout_35.addWidget(self.setting_cutoff_game_over_music)

        self.setting_remove_enemy_music = RandoTriStateCheckBox(self.audio_cosmetics_group_box)
        self.setting_remove_enemy_music.setObjectName(u"setting_remove_enemy_music")

        self.verticalLayout_35.addWidget(self.setting_remove_enemy_music)

        self.low_health_beeping_speed_label = QLabel(self.audio_cosmetics_group_box)
        self.low_health_beeping_speed_label.setObjectName(u"low_health_beeping_speed_label")

        self.verticalLayout_35.addWidget(self.low_health_beeping_speed_label)

        self.setting_low_health_beeping_speed = QComboBox(self.audio_cosmetics_group_box)
        self.setting_low_health_beeping_speed.setObjectName(u"setting_low_health_beeping_speed")

        self.verticalLayout_35.addWidget(self.setting_low_health_beeping_speed)


        self.verticalLayout_10.addWidget(self.audio_cosmetics_group_box)

        self.environment_cosmetics_group_box = QGroupBox(self.cosmetics_tab)
        self.environment_cosmetics_group_box.setObjectName(u"environment_cosmetics_group_box")
        self.verticalLayout_33 = QVBoxLayout(self.environment_cosmetics_group_box)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.setting_starry_skies = RandoTriStateCheckBox(self.environment_cosmetics_group_box)
        self.setting_starry_skies.setObjectName(u"setting_starry_skies")

        self.verticalLayout_33.addWidget(self.setting_starry_skies)

        self.daytime_sky_color_label = QLabel(self.environment_cosmetics_group_box)
        self.daytime_sky_color_label.setObjectName(u"daytime_sky_color_label")

        self.verticalLayout_33.addWidget(self.daytime_sky_color_label)

        self.setting_daytime_sky_color = QComboBox(self.environment_cosmetics_group_box)
        self.setting_daytime_sky_color.setObjectName(u"setting_daytime_sky_color")

        self.verticalLayout_33.addWidget(self.setting_daytime_sky_color)

        self.nighttime_sky_color_label = QLabel(self.environment_cosmetics_group_box)
        self.nighttime_sky_color_label.setObjectName(u"nighttime_sky_color_label")

        self.verticalLayout_33.addWidget(self.nighttime_sky_color_label)

        self.setting_nighttime_sky_color = QComboBox(self.environment_cosmetics_group_box)
        self.setting_nighttime_sky_color.setObjectName(u"setting_nighttime_sky_color")

        self.verticalLayout_33.addWidget(self.setting_nighttime_sky_color)

        self.daytime_cloud_color_label = QLabel(self.environment_cosmetics_group_box)
        self.daytime_cloud_color_label.setObjectName(u"daytime_cloud_color_label")

        self.verticalLayout_33.addWidget(self.daytime_cloud_color_label)

        self.setting_daytime_cloud_color = QComboBox(self.environment_cosmetics_group_box)
        self.setting_daytime_cloud_color.setObjectName(u"setting_daytime_cloud_color")

        self.verticalLayout_33.addWidget(self.setting_daytime_cloud_color)

        self.nighttime_cloud_color_label = QLabel(self.environment_cosmetics_group_box)
        self.nighttime_cloud_color_label.setObjectName(u"nighttime_cloud_color_label")

        self.verticalLayout_33.addWidget(self.nighttime_cloud_color_label)

        self.setting_nighttime_cloud_color = QComboBox(self.environment_cosmetics_group_box)
        self.setting_nighttime_cloud_color.setObjectName(u"setting_nighttime_cloud_color")

        self.verticalLayout_33.addWidget(self.setting_nighttime_cloud_color)


        self.verticalLayout_10.addWidget(self.environment_cosmetics_group_box)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_10)

        self.tab_widget.addTab(self.cosmetics_tab, "")
        self.advanced_tab = QWidget()
        self.advanced_tab.setObjectName(u"advanced_tab")
        sizePolicy1.setHeightForWidth(self.advanced_tab.sizePolicy().hasHeightForWidth())
        self.advanced_tab.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.advanced_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.file_setup_group_box = QGroupBox(self.advanced_tab)
        self.file_setup_group_box.setObjectName(u"file_setup_group_box")
        sizePolicy.setHeightForWidth(self.file_setup_group_box.sizePolicy().hasHeightForWidth())
        self.file_setup_group_box.setSizePolicy(sizePolicy)
        self.verticalLayout_31 = QVBoxLayout(self.file_setup_group_box)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.open_folders_label = QLabel(self.file_setup_group_box)
        self.open_folders_label.setObjectName(u"open_folders_label")

        self.verticalLayout_31.addWidget(self.open_folders_label)

        self.open_output_folder_button = QPushButton(self.file_setup_group_box)
        self.open_output_folder_button.setObjectName(u"open_output_folder_button")

        self.verticalLayout_31.addWidget(self.open_output_folder_button)

        self.open_extract_folder_button = QPushButton(self.file_setup_group_box)
        self.open_extract_folder_button.setObjectName(u"open_extract_folder_button")

        self.verticalLayout_31.addWidget(self.open_extract_folder_button)

        self.utils_hline_2 = QFrame(self.file_setup_group_box)
        self.utils_hline_2.setObjectName(u"utils_hline_2")
        self.utils_hline_2.setFrameShape(QFrame.Shape.HLine)
        self.utils_hline_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.utils_hline_2)

        self.output_label = QLabel(self.file_setup_group_box)
        self.output_label.setObjectName(u"output_label")
        sizePolicy.setHeightForWidth(self.output_label.sizePolicy().hasHeightForWidth())
        self.output_label.setSizePolicy(sizePolicy)

        self.verticalLayout_31.addWidget(self.output_label)

        self.config_output = QLineEdit(self.file_setup_group_box)
        self.config_output.setObjectName(u"config_output")
        self.config_output.setReadOnly(True)

        self.verticalLayout_31.addWidget(self.config_output)

        self.output_button_layout = QHBoxLayout()
        self.output_button_layout.setObjectName(u"output_button_layout")
        self.reset_output_button = QPushButton(self.file_setup_group_box)
        self.reset_output_button.setObjectName(u"reset_output_button")

        self.output_button_layout.addWidget(self.reset_output_button)

        self.browse_output_button = QPushButton(self.file_setup_group_box)
        self.browse_output_button.setObjectName(u"browse_output_button")

        self.output_button_layout.addWidget(self.browse_output_button)


        self.verticalLayout_31.addLayout(self.output_button_layout)

        self.utils_hline_3 = QFrame(self.file_setup_group_box)
        self.utils_hline_3.setObjectName(u"utils_hline_3")
        self.utils_hline_3.setFrameShape(QFrame.Shape.HLine)
        self.utils_hline_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.utils_hline_3)

        self.verify_extract_label = QLabel(self.file_setup_group_box)
        self.verify_extract_label.setObjectName(u"verify_extract_label")

        self.verticalLayout_31.addWidget(self.verify_extract_label)

        self.verify_extract_layout = QHBoxLayout()
        self.verify_extract_layout.setObjectName(u"verify_extract_layout")
        self.verify_important_extract_button = QPushButton(self.file_setup_group_box)
        self.verify_important_extract_button.setObjectName(u"verify_important_extract_button")

        self.verify_extract_layout.addWidget(self.verify_important_extract_button)

        self.verify_all_extract_button = QPushButton(self.file_setup_group_box)
        self.verify_all_extract_button.setObjectName(u"verify_all_extract_button")

        self.verify_extract_layout.addWidget(self.verify_all_extract_button)


        self.verticalLayout_31.addLayout(self.verify_extract_layout)

        self.other_mods_group_box = QGroupBox(self.file_setup_group_box)
        self.other_mods_group_box.setObjectName(u"other_mods_group_box")
        sizePolicy.setHeightForWidth(self.other_mods_group_box.sizePolicy().hasHeightForWidth())
        self.other_mods_group_box.setSizePolicy(sizePolicy)
        self.verticalLayout_42 = QVBoxLayout(self.other_mods_group_box)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.other_mods_explanation_text = QLabel(self.other_mods_group_box)
        self.other_mods_explanation_text.setObjectName(u"other_mods_explanation_text")
        self.other_mods_explanation_text.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.other_mods_explanation_text)

        self.other_mods_scroll_area = QScrollArea(self.other_mods_group_box)
        self.other_mods_scroll_area.setObjectName(u"other_mods_scroll_area")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.other_mods_scroll_area.sizePolicy().hasHeightForWidth())
        self.other_mods_scroll_area.setSizePolicy(sizePolicy6)
        self.other_mods_scroll_area.setWidgetResizable(True)
        self.other_mods_scroll_widget = QWidget()
        self.other_mods_scroll_widget.setObjectName(u"other_mods_scroll_widget")
        self.other_mods_scroll_widget.setGeometry(QRect(0, 0, 419, 208))
        self.other_mods_scroll_layout = QVBoxLayout(self.other_mods_scroll_widget)
        self.other_mods_scroll_layout.setObjectName(u"other_mods_scroll_layout")
        self.other_mods_scroll_area.setWidget(self.other_mods_scroll_widget)

        self.horizontalLayout_7.addWidget(self.other_mods_scroll_area)


        self.verticalLayout_42.addLayout(self.horizontalLayout_7)

        self.other_mods_button_layout = QHBoxLayout()
        self.other_mods_button_layout.setObjectName(u"other_mods_button_layout")
        self.open_other_mods_dir_button = QPushButton(self.other_mods_group_box)
        self.open_other_mods_dir_button.setObjectName(u"open_other_mods_dir_button")

        self.other_mods_button_layout.addWidget(self.open_other_mods_dir_button)

        self.refresh_mod_list_button = QPushButton(self.other_mods_group_box)
        self.refresh_mod_list_button.setObjectName(u"refresh_mod_list_button")

        self.other_mods_button_layout.addWidget(self.refresh_mod_list_button)


        self.verticalLayout_42.addLayout(self.other_mods_button_layout)


        self.verticalLayout_31.addWidget(self.other_mods_group_box)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_2)


        self.verticalLayout_9.addWidget(self.file_setup_group_box)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.tab_widget.addTab(self.advanced_tab, "")

        self.verticalLayout_2.addWidget(self.tab_widget)

        self.settings_descriptions_layout = QHBoxLayout()
        self.settings_descriptions_layout.setObjectName(u"settings_descriptions_layout")
        self.settings_current_option_description_label = QLabel(self.central_widget)
        self.settings_current_option_description_label.setObjectName(u"settings_current_option_description_label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.settings_current_option_description_label.sizePolicy().hasHeightForWidth())
        self.settings_current_option_description_label.setSizePolicy(sizePolicy7)
        self.settings_current_option_description_label.setMinimumSize(QSize(0, 64))
        self.settings_current_option_description_label.setTextFormat(Qt.TextFormat.RichText)
        self.settings_current_option_description_label.setWordWrap(True)

        self.settings_descriptions_layout.addWidget(self.settings_current_option_description_label)

        self.settings_default_option_description_label = QLabel(self.central_widget)
        self.settings_default_option_description_label.setObjectName(u"settings_default_option_description_label")
        sizePolicy7.setHeightForWidth(self.settings_default_option_description_label.sizePolicy().hasHeightForWidth())
        self.settings_default_option_description_label.setSizePolicy(sizePolicy7)
        self.settings_default_option_description_label.setMinimumSize(QSize(0, 64))
        self.settings_default_option_description_label.setWordWrap(True)

        self.settings_descriptions_layout.addWidget(self.settings_default_option_description_label)


        self.verticalLayout_2.addLayout(self.settings_descriptions_layout)

        self.footer_buttons = QHBoxLayout()
        self.footer_buttons.setObjectName(u"footer_buttons")
        self.about_button = QPushButton(self.central_widget)
        self.about_button.setObjectName(u"about_button")

        self.footer_buttons.addWidget(self.about_button)

        self.footer_hspacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footer_buttons.addItem(self.footer_hspacer2)

        self.reset_settings_to_default_button = QPushButton(self.central_widget)
        self.reset_settings_to_default_button.setObjectName(u"reset_settings_to_default_button")
        sizePolicy5.setHeightForWidth(self.reset_settings_to_default_button.sizePolicy().hasHeightForWidth())
        self.reset_settings_to_default_button.setSizePolicy(sizePolicy5)

        self.footer_buttons.addWidget(self.reset_settings_to_default_button)

        self.footer_hspacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footer_buttons.addItem(self.footer_hspacer1)

        self.patch_button = QPushButton(self.central_widget)
        self.patch_button.setObjectName(u"patch_button")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.patch_button.sizePolicy().hasHeightForWidth())
        self.patch_button.setSizePolicy(sizePolicy8)

        self.footer_buttons.addWidget(self.patch_button)


        self.verticalLayout_2.addLayout(self.footer_buttons)

        main_window.setCentralWidget(self.central_widget)

        self.retranslateUi(main_window)

        self.tab_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"The Legend of Zelda: Skyward Sword HD Tweaks", None))
        self.how_to_group_box.setTitle(QCoreApplication.translate("main_window", u"How to Modify the Game", None))
        self.how_to_extract_label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p><span style=\" font-weight:700;\">Extract the Game</span>:</p><p>Before modifying the base game, you need to have a valid extract of the 1.0.1 version of the game.</p><p>Please follow our handy setup guides for the <a href=\"https://docs.google.com/document/d/1VXNME7SVD5EU7NNn9dQ15_Q9-v9OJAHOX-hSor0n2dg\"><span style=\" text-decoration: underline; color:#9a0089;\">Nintendo Switch console</span></a> or for <a href=\"https://docs.google.com/document/d/1HHQRXND0n-ZrmhEl4eXjzMANQ-xHK3pKKXPQqSbwXwY\"><span style=\" text-decoration: underline; color:#9a0089;\">emulator</span></a>.</p></body></html>", None))
        self.choose_settings_label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p><span style=\" font-weight:700;\">Select your Tweaks:</span></p><p>Go to the &quot;Tweaks&quot; tab and select your choices!</p></body></html>", None))
        self.how_to_generate_label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p><span style=\" font-weight:700;\">Patch the Game</span>:</p><p>Once you're ready, click the <span style=\" font-family:'Courier New';\">Patch</span> button in the bottom right. The program will begin to generate a game patch with your selected tweaks and mods.</p></body></html>", None))
        self.how_to_running_label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p><span style=\" font-weight:700;\">Play the Game</span>:</p><p>You can play the modified game either on a modded Nintendo Switch console or on an emulator.</p><p>Please follow the instructions in our setup guides for <a href=\"https://docs.google.com/document/d/1VXNME7SVD5EU7NNn9dQ15_Q9-v9OJAHOX-hSor0n2dg\"><span style=\" text-decoration: underline; color:#9a0089;\">Nintendo Switch console</span></a> or for <a href=\"https://docs.google.com/document/d/1HHQRXND0n-ZrmhEl4eXjzMANQ-xHK3pKKXPQqSbwXwY\"><span style=\" text-decoration: underline; color:#9a0089;\">emulator</span></a> to find instructions on running your patch.</p><p>For additional help with this process, please join the <a href=\"https://discord.gg/nNbpfH5jyG\"><span style=\" text-decoration: underline; color:#9a0089;\">Discord Server</span></a> or ask on <a href=\"https://github.com/mint-choc-chip-skyblade/sshd-rando/issues\"><span style=\" text-decoration: underline; color:#9a0089;\">GitHub</span></a>.</p></body></html>", None))
        self.useful_info_group_box.setTitle(QCoreApplication.translate("main_window", u"Useful Information", None))
        self.guides_label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p>Guides</p><p>\u279c <a href=\"https://docs.google.com/document/d/1VXNME7SVD5EU7NNn9dQ15_Q9-v9OJAHOX-hSor0n2dg\"><span style=\" text-decoration: underline; color:#9a0089;\">Setup Guide (Console)</span></a><br/>\u279c <a href=\"https://docs.google.com/document/d/1HHQRXND0n-ZrmhEl4eXjzMANQ-xHK3pKKXPQqSbwXwY\"><span style=\" text-decoration: underline; color:#9a0089;\">Setup Guide (Emulator)</span></a><br/>\u279c <a href=\"https://docs.google.com/document/d/1Dm0jhwXWIvPLuvl-JoRqocTKjXM_jRRmryYqpQMO_6w\"><span style=\" text-decoration: underline; color:#9a0089;\">Tricks Guide</span></a><br/>\u279c <a href=\"https://docs.google.com/document/d/1Eq1rXcjwRpVjp-5ugpQAsjmZy5QuGi7KAOkvpWoQkqc\"><span style=\" text-decoration: underline; color:#9a0089;\">Texture Replacement Guide</span></a></p></body></html>", None))
        self.community_label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p>Community</p><p><span style=\" font-weight:700;\">\u279c </span><a href=\"https://discord.gg/nNbpfH5jyG\"><span style=\" text-decoration: underline; color:#9a0089;\">Discord Server</span></a><br/><span style=\" font-weight:700;\">\u279c </span><a href=\"https://github.com/mint-choc-chip-skyblade/sshd-rando/issues\"><span style=\" text-decoration: underline; color:#9a0089;\">Report a Bug</span></a><br/><span style=\" font-weight:700;\">\u279c </span><a href=\"https://github.com/mint-choc-chip-skyblade/sshd-rando\"><span style=\" text-decoration: underline; color:#9a0089;\">GitHub</span></a></p></body></html>", None))
        self.accessibility_group_box.setTitle(QCoreApplication.translate("main_window", u"Accessibility", None))
        self.theming_fonts.setTitle(QCoreApplication.translate("main_window", u"Fonts", None))
        self.font_family_label.setText(QCoreApplication.translate("main_window", u"Font Family", None))
        self.font_family_combo_box.setPlaceholderText(QCoreApplication.translate("main_window", u"Select Font Family", None))
        self.font_size_label.setText(QCoreApplication.translate("main_window", u"Font Size", None))
        self.font_reset_button.setText(QCoreApplication.translate("main_window", u"Reset", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.getting_started_tab), QCoreApplication.translate("main_window", u"Getting Started", None))
        self.dungeons_group_box.setTitle(QCoreApplication.translate("main_window", u"Tweaks", None))
        self.boss_key_puzzles_label.setText(QCoreApplication.translate("main_window", u"Boss Key Puzzles", None))
        self.setting_spawn_hearts.setText(QCoreApplication.translate("main_window", u"Spawn Hearts and Heart Flowers", None))
        self.setting_upgraded_skyward_strike.setText(QCoreApplication.translate("main_window", u"Upgraded Skyward Strike", None))
        self.setting_faster_air_meter_depletion.setText(QCoreApplication.translate("main_window", u"Faster Air Meter Depletion", None))
        self.damage_multiplier_label.setText(QCoreApplication.translate("main_window", u"Damage Multiplier", None))
        self.ammo_availability_label.setText(QCoreApplication.translate("main_window", u"Ammo Availability", None))
        self.minigame_difficulty_label.setText(QCoreApplication.translate("main_window", u"Minigame Difficulty", None))
        self.random_trial_object_positions_label.setText(QCoreApplication.translate("main_window", u"Random Trial Object Positions", None))
        self.other_settings_group_box.setTitle(QCoreApplication.translate("main_window", u"Other Settings", None))
        self.setting_enable_back_in_time.setText(QCoreApplication.translate("main_window", u"Enable Back in Time (BiT)", None))
        self.setting_allow_flying_at_night.setText(QCoreApplication.translate("main_window", u"Allow Flying at Night", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tweaks_tab), QCoreApplication.translate("main_window", u"Tweaks", None))
        self.player_cosmetics_group_box.setTitle(QCoreApplication.translate("main_window", u"Player Cosmetics", None))
        self.setting_tunic_swap.setText(QCoreApplication.translate("main_window", u"Tunic Swap", None))
        self.setting_lightning_skyward_strike.setText(QCoreApplication.translate("main_window", u"Lightning Skyward Strike", None))
        self.audio_cosmetics_group_box.setTitle(QCoreApplication.translate("main_window", u"Audio Cosmetics", None))
        self.randomize_music_label.setText(QCoreApplication.translate("main_window", u"Randomize Music", None))
        self.setting_cutoff_game_over_music.setText(QCoreApplication.translate("main_window", u"Cutoff Game Over Music", None))
        self.setting_remove_enemy_music.setText(QCoreApplication.translate("main_window", u"Remove Enemy Music", None))
        self.low_health_beeping_speed_label.setText(QCoreApplication.translate("main_window", u"Low Health Beeping Speed", None))
        self.environment_cosmetics_group_box.setTitle(QCoreApplication.translate("main_window", u"Environment Cosmetics", None))
        self.setting_starry_skies.setText(QCoreApplication.translate("main_window", u"Starry Skies", None))
        self.daytime_sky_color_label.setText(QCoreApplication.translate("main_window", u"Daytime Sky Color", None))
        self.nighttime_sky_color_label.setText(QCoreApplication.translate("main_window", u"Nighttime Sky Color", None))
        self.daytime_cloud_color_label.setText(QCoreApplication.translate("main_window", u"Daytime Cloud Color", None))
        self.nighttime_cloud_color_label.setText(QCoreApplication.translate("main_window", u"Nighttime Cloud Color", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.cosmetics_tab), QCoreApplication.translate("main_window", u"Cosmetics", None))
        self.file_setup_group_box.setTitle(QCoreApplication.translate("main_window", u"Extract and Output Utilities", None))
        self.open_folders_label.setText(QCoreApplication.translate("main_window", u"Open Folders", None))
        self.open_output_folder_button.setText(QCoreApplication.translate("main_window", u"Open Output Folder", None))
        self.open_extract_folder_button.setText(QCoreApplication.translate("main_window", u"Open Extract Folder", None))
        self.output_label.setText(QCoreApplication.translate("main_window", u"Output Path:", None))
        self.reset_output_button.setText(QCoreApplication.translate("main_window", u"Reset", None))
        self.browse_output_button.setText(QCoreApplication.translate("main_window", u"Browse", None))
        self.verify_extract_label.setText(QCoreApplication.translate("main_window", u"Verify Extracted Game Files:", None))
        self.verify_important_extract_button.setText(QCoreApplication.translate("main_window", u"Verify Important Files", None))
        self.verify_all_extract_button.setText(QCoreApplication.translate("main_window", u"Verify All Files", None))
        self.other_mods_group_box.setTitle(QCoreApplication.translate("main_window", u"Other Mods", None))
        self.other_mods_explanation_text.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p>To ensure any other mods you wish to use play nicely with each other, put them in separate folders in the <span style=\" font-weight:700;\">other_mods</span> directory and choose which ones you want to apply together.</p><p>For example, if you have a mod which changes Link's tunic color, you can create a new folder in the <span style=\" font-weight:700;\">other_mods</span> directory named &quot;Other Tunic Color&quot; and put the <span style=\" font-weight:700;\">romfs</span> folder of that mod into the new folder. Then refresh the mod list and it should appear below. We do not currently support mods that modify any files in the <span style=\" font-weight:700;\">exefs</span> folder.</p></body></html>", None))
        self.open_other_mods_dir_button.setText(QCoreApplication.translate("main_window", u"Open other_mods Folder", None))
        self.refresh_mod_list_button.setText(QCoreApplication.translate("main_window", u"Refresh Mod List", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.advanced_tab), QCoreApplication.translate("main_window", u"Advanced", None))
        self.settings_current_option_description_label.setText(QCoreApplication.translate("main_window", u"Settings current option description", None))
        self.settings_default_option_description_label.setText(QCoreApplication.translate("main_window", u"Settings default option description", None))
        self.about_button.setText(QCoreApplication.translate("main_window", u"About", None))
        self.reset_settings_to_default_button.setText(QCoreApplication.translate("main_window", u"Reset Settings to Default", None))
        self.patch_button.setText(QCoreApplication.translate("main_window", u"Patch", None))
    # retranslateUi

