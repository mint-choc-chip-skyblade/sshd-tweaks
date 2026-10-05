; Never show Fi text for low health
; onlyif reduce_fi_text == on
.offset 0x7100dc4724
mov w0, #1

; Never show Fi text for full wallet
; onlyif reduce_fi_text == on
.offset 0x7100dc4810
mov w0, #1
