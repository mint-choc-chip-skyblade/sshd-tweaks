#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(unused)]

use crate::actor;
use crate::debug;
use crate::flag;
use crate::input;
use crate::savefile;
use crate::settings;

use core::arch::asm;
use core::ffi::{c_char, c_int, c_void};
use static_assertions::assert_eq_size;
use wchar::wch;

// repr(C) prevents rust from reordering struct fields.
// packed(1) prevents rust from aligning structs to the size of the largest
// field.

// Using u64 or 64bit pointers forces structs to be 8-byte aligned.
// The vanilla code seems to be 4-byte aligned. To make extra sure, used
// packed(1) to force the alignment to match what you define.

// Always add an assert_eq_size!() macro after defining a struct to ensure it's
// the size you expect it to be.

// Lyt stuff
#[repr(C, packed(1))]
#[derive(Copy, Clone)]
pub struct dLytMsgWindow {
    pub _0:       [u8; 0xA90],
    pub text_mgr: *mut TextMgr,
}
assert_eq_size!([u8; 0xA98], dLytMsgWindow);

#[repr(C, packed(1))]
#[derive(Copy, Clone)]
pub struct dLytPauseDisp {
    pub _0:        [u8; 0xC5E],
    pub is_paused: bool,
    pub _1:        [u8; 0x11],
}
assert_eq_size!([u8; 0xC70], dLytPauseDisp);

#[repr(C, packed(1))]
#[derive(Copy, Clone)]
pub struct dLytSaveMgr {
    pub base:                   [u8; 0xC0],
    pub state_mgr:              actor::StateMgr,
    pub save_msg_window:        [u8; 0x23A8],
    pub save_text_prompt_index: u32,
    pub state_select_related:   u32,
    pub _0:                     [u8; 14],
    pub save_obj_name_index:    u8,
    pub saving:                 bool,
    pub is_not_saving:          bool,
    pub _1:                     [u8; 7],
}
assert_eq_size!([u8; 0x24F8], dLytSaveMgr);

// Text stuff
#[repr(C, packed(1))]
#[derive(Copy, Clone)]
pub struct TextMgr {
    pub _0:                 [u8; 0x8AC],
    pub numeric_args:       [u32; 10],
    pub num_args_copy:      [u32; 10],
    pub _1:                 [u8; 0x20],
    pub vertical_scale:     f32,
    pub cursor_pos_y:       f32,
    pub msg_window_subtype: u8,
    pub _2:                 [u8; 0xCF],
    pub command_insert:     i32,
    pub string_args:        [[u16; 64]; 4],
}
assert_eq_size!([u8; 0xBF8], TextMgr);

// IMPORTANT: when using vanilla code, the start point must be declared in
// symbols.yaml and then added to this extern block.
extern "C" {
    static mut CURRENT_STAGE_NAME: [u8; 8];
    static dManager__sInstance: *mut c_void;
    static GLOBAL_TEXT_MGR: *mut TextMgr;
    static FILE_MGR: *mut savefile::FileMgr;
    static RANDOMIZER_SETTINGS: settings::RandomizerSettings;

    static dLytSaveMgr__sSavePrompts: [*const c_char; 6];

    // Functions
    fn debugPrint_32(string: *const c_char, fstr: *const c_char, ...);
    fn set_string_arg(text_mgr: *mut TextMgr, arg: *const c_void, arg_num: u32);
    fn getTextMessageByLabel(
        param1: *mut c_void,
        param2: *mut c_void,
        param3: u32,
        param4: u32,
        param5: u32,
    ) -> *mut c_void;
    fn eventFlowTextProcessingRelated(
        param1: *mut c_void,
        param2: *mut c_void,
        text_string: *mut c_void,
        buffer: *mut c_void,
        buffer_size: i32,
        param6: u64,
    );
    fn get_msb_text_maybe(msbt_info: *mut c_void, tutorial_text_name: *mut c_void) -> *mut c_void;
    fn dLytHelp__stateNoneUpdate(dLytHelp: *mut c_void);
}

// IMPORTANT: when adding functions here that need to get called from the game,
// add `#[no_mangle]` and add a .global *symbolname* to
// additions/rust-additions.asm
