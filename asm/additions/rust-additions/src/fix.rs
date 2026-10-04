#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(unused)]

use crate::actor;
use crate::debug;
use crate::flag;
use crate::lyt;
use crate::minigame;
use crate::player;

use core::arch::asm;
use core::ffi::{c_char, c_void};
use static_assertions::assert_eq_size;

// repr(C) prevents rust from reordering struct fields.
// packed(1) prevents rust from aligning structs to the size of the largest
// field.

// Using u64 or 64bit pointers forces structs to be 8-byte aligned.
// The vanilla code seems to be 4-byte aligned. To make extra sure, used
// packed(1) to force the alignment to match what you define.

// Always add an assert_eq_size!() macro after defining a struct to ensure it's
// the size you expect it to be.

//////////////////////
// ADD STRUCTS HERE //
//////////////////////

// IMPORTANT: when using vanilla code, the start point must be declared in
// symbols.yaml and then added to this extern block.
extern "C" {
    static PLAYER_PTR: *mut player::dPlayer;
    static LOFTWING_PTR: *mut player::dBird;

    static STORYFLAG_MGR: *mut flag::FlagMgr;
    static SCENEFLAG_MGR: *mut flag::SceneflagMgr;

    static mut CURRENT_STAGE_NAME: [u8; 8];

    static LYT_MSG_WINDOW: *mut lyt::dLytMsgWindow;

    // Functions
    fn debugPrint_128(string: *const c_char, fstr: *const c_char, ...);
    fn strlen(string: *mut u8) -> u64;
    fn strncmp(dest: *mut u8, src: *mut u8, size: u64) -> u64;
    fn dAcOlightLine__inUpdate(light_pillar_actor: *mut actor::dAcOlightLine, unk: u64);
    fn dAcOrdinaryNpc__update(npc: *mut c_void) -> u64;
    fn dAcNpcSkn2__addInteractionTarget(horwell: *mut c_void, some_val: u32);
    fn allocateActorWork1Heap(
        param1: *mut actor::dAcOBase,
        param2: i32,
        param3: *mut c_char,
    ) -> u64;
}

// IMPORTANT: when adding functions here that need to get called from the game,
// add `#[no_mangle]` and add a .global *symbolname* to
// additions/rust-additions.asm
#[no_mangle]
pub extern "C" fn remove_timeshift_stone_cutscenes() {
    unsafe {
        let mut subtypeBitfield: u8;
        asm!(
            "ldrb {0:w}, [x23, #0xce]",
            out(reg) subtypeBitfield,
        );

        // If not Sandship stone
        if (subtypeBitfield & 2) == 0 {
            asm!(
                "mov w8, #0",
                "strb w8, [x23, #0xba]", // playFirstTimeCS
                "strb w8, [x23, #0xc1]", // isFirstStone
            );
        }

        // Replaced instructions
        asm!(
            "mov w9, #0xc2960000",
            "mov w8, {0:w}",
            in(reg) subtypeBitfield,
        );
    }
}

#[no_mangle]
pub extern "C" fn apply_loftwing_speed_override() {
    unsafe {
        if (&CURRENT_STAGE_NAME[..5] == b"F023\0"
            && flag::check_storyflag(368) == 1 // Pumpkin Soup delivered to rainbow island
            && flag::check_storyflag(200) == 0) // Levias defeated
            || minigame::MinigameState::SpiralChargeTutorial.is_current()
        {
            if !LOFTWING_PTR.is_null() && (*LOFTWING_PTR).obj_base_members.forward_speed > 80.0 {
                (*LOFTWING_PTR).obj_base_members.forward_speed = 80.0;
            }
        }
    }
}
