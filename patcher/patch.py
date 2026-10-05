from constants.verificationconstants import *
from filepathconstants import CONFIG_PATH
from logic.generate import generate
from patches.allpatchhandler import AllPatchHandler
from patcher.verify_extract import verify_extract
from util.arguments import get_program_args
from gui.dialogs.dialog_header import update_progress_value


def patch():
    print("Starting new patch:")
    args = get_program_args()

    if not args.dryrun:
        update_progress_value(0)
        verify_extract()

    update_progress_value(5)
    world = generate(CONFIG_PATH)

    if not args.dryrun:
        patch_handler = AllPatchHandler(world)
        patch_handler.do_all_patches()

    print("Patching complete!")
    update_progress_value(100)

    if not args.dryrun:
        print(f"The patch can be found at: {world.config.output_dir.as_posix()}")
