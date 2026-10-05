; Always allow using L to nock an arrow
; onlyif quick_draw_bow == on
.offset 0x7100a5f668
nop

; Holding L automatically quick charges the bow
; onlyif quick_draw_bow == on
.offset 0x7100a60578
mov w8, #0x2006
