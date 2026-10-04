#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(unused)]

use crate::debug;
use crate::flag;
use crate::settings;

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

#[repr(C, packed(1))]
#[derive(Copy, Clone)]
pub struct SndAudioMgr {
    pub vtable:     *mut SndAudioMgrVtable,
    pub _0:         [u8; 0xCE0],
    pub brsar_info: *mut BrsarInfo,
}

#[repr(C, packed(1))]
#[derive(Copy, Clone)]
pub struct SndAudioMgrVtable {
    pub _0:  [u8; 0x48],
    pub fn9: extern "C" fn(*mut SndAudioMgr, i32, u64, u64),
}

#[repr(C, packed(1))]
#[derive(Copy, Clone)]
pub struct BrsarInfo {
    pub _0:       [u8; 0x87E1C],
    pub wzs_data: [WZSInfo; 238],
}

#[repr(C, packed(1))]
#[derive(Copy, Clone)]
pub struct WZSInfo {
    pub audio_len:       i32,
    pub blank:           i32,
    pub negative_one:    i32,
    pub unk1:            i32,
    pub unk_offset1:     i32,
    pub unk2:            i32,
    pub unk_offset2:     i32,
    pub filename_prefix: [c_char; 4],
    pub filename:        [c_char; 32],
    pub pad:             u32,
}
assert_eq_size!([u8; 0x44], WZSInfo);

// IMPORTANT: when using vanilla code, the start point must be declared in
// symbols.yaml and then added to this extern block.
extern "C" {
    static SndAudioMgr__sInstance: *mut SndAudioMgr;
    static BGM_SOUND_MGR: *mut c_void;
    static RANDOM_MUSIC_DATA: [[c_char; 32]; 238];
    static RANDOMIZER_SETTINGS: settings::RandomizerSettings;

    static mut CURRENT_STAGE_NAME: [u8; 8];
    static mut CURRENT_LAYER: u8;

    // Functions
    fn debugPrint_128(string: *const c_char, fstr: *const c_char, ...);
}

// IMPORTANT: when adding functions here that need to get called from the game,
// add `#[no_mangle]` and add a .global *symbolname* to
// additions/rust-additions.asm
#[no_mangle]
pub extern "C" fn randomize_music() {
    unsafe {
        let wzs_data_array = (*(*SndAudioMgr__sInstance).brsar_info).wzs_data;
        let mut index = 0;
        while index < 238 {
            (*(*SndAudioMgr__sInstance).brsar_info).wzs_data[index].filename =
                RANDOM_MUSIC_DATA[index];

            if index != 2 || RANDOMIZER_SETTINGS.cutoff_game_over_music == 0 {
                (*(*SndAudioMgr__sInstance).brsar_info).wzs_data[index].audio_len = 0x7FFFFFFF;
            }

            index += 1;
        }

        // Replaced instructions
        asm!("mov x11, x19", "mov x10, {0:x}", in(reg) BGM_SOUND_MGR);
    }
}
