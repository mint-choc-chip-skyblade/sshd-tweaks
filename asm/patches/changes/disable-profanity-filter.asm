; Skip over profanity filter checking stuff
; onlyif no_profanity_filter == on
.offset 0x7100028c20
b 0x7100028d94

; Always act like input is valid
; onlyif no_profanity_filter == on
.offset 0x7100028d98
mov w0, #0
