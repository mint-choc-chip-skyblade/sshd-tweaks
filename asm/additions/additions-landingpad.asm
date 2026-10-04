; Start using subsdk8 0x500 bytes into the .text section
; Please leave 0x1000 bytes for this landingpad

; Yes, this in not very optimal. However, this big comparison chain is easier
; to edit and harder to mess up than a more elegant solution. In particular,
; this method makes it very easy to remove functions without having to change
; `w8` across the codebase.

.offset 0x712e0a5500
; startflags
cmp w8, #2
b.eq handle_startflags

cmp w8, #14
b.eq drop_arrows_bombs_seeds

cmp w8, #15
b.eq drop_nothing

cmp w8, #18
b.eq remove_timeshift_stone_cutscenes

cmp w8, #20
b.eq custom_event_commands

cmp w8, #37
b.eq set_correct_boss_key_positions

cmp w8, #38
b.eq set_random_boss_key_positions

cmp w8, #42
b.eq try_end_pumpkin_archery

cmp w8, #49
b.eq main_loop_inject

cmp w8, #50
b.eq activate_back_in_time

cmp w8, #54
b.eq init_rainbow_colors

cmp w8, #79
b.eq check_local_sceneflag

cmp w8, #81
b.eq fix_memory_leak

cmp w8, #82
b.eq load_custom_bzs

cmp w8, #83
b.eq use_custom_bzs

cmp w8, #94
b.eq randomize_music

cmp w8, #95
b.eq prefer_object_folder_for_stage_arcs

cmp w8, #96
b.eq setup_registers_for_general_modreplace

cmp w8, #97
b.eq prefer_modreplace_for_general_arcs

ret ; this should never be reached

; ends at 0x712e0a7000
