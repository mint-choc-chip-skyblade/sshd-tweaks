from .config import Config
from .settings import *
from util.text import *

from collections import Counter, OrderedDict
from typing import TYPE_CHECKING
import logging
import yaml

if TYPE_CHECKING:
    from .search import Search


class MissingInfoError(RuntimeError):
    pass


class WrongInfoError(RuntimeError):
    pass


class World:
    event_id_counter: int = 0
    area_id_counter: int = 0

    def __init__(self, id_: int) -> None:
        self.id = id_
        self.config: Config = None  # type: ignore
        self.num_worlds: int = 0
        self.worlds: list["World"] = []

        self.setting_map: SettingMap = SettingMap()

    def __str__(self) -> str:
        return f"World {self.id + 1}"

    def resolve_random_settings(self) -> None:
        # Use the randomness from the seed for resolving standard settings
        for setting in self.setting_map.settings.values():
            if setting.info.type == SettingType.STANDARD:
                setting.resolve_if_random()

    def resolve_conflicting_settings(self) -> None:
        pass

    def setting(self, setting_name: str) -> SettingGet:
        if setting_name not in self.setting_map.settings:
            raise SettingInfoError(
                f'No Setting named "{setting_name}" in settings for {self}'
            )
        return SettingGet(setting_name, self.setting_map.settings[setting_name])
