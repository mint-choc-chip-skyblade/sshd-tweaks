import os
import sys
import time

from filepathconstants import (
    SSHD_EXTRACT_PATH,
    OTHER_MODS_PATH,
)
from util.arguments import get_program_args
import logging

args = get_program_args()

# Set specified log level
if args.debug:
    print("Starting Debug Log")
    logging.basicConfig(
        filename="debug.log",
        encoding="utf-8",
        level=logging.DEBUG,
        filemode="w",
    )

# Ensure the necessary directories are created
if not SSHD_EXTRACT_PATH.exists():
    SSHD_EXTRACT_PATH.mkdir()

if not OTHER_MODS_PATH.exists():
    OTHER_MODS_PATH.mkdir()

# Imports here to prevent circular dependency
if not args.nogui:
    from gui.main import start_gui

    if __name__ == "__main__":
        # Before starting the gui, setup exception handling
        from PySide6.QtWidgets import QApplication
        from gui.dialogs.error_dialog import error

        # Adding these lines helps fix the GUI on Retina displays
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        app = QApplication(sys.argv + ["--style", "fusion"])

        try:
            start_gui(app)
        except Exception as e:
            error(e)
else:
    from patcher.patch import patch

    if __name__ == "__main__":
        start_patch_time = time.perf_counter()

        patch()

        print(
            f"Total patch took {(time.perf_counter() - start_patch_time)} seconds"
        )
