define hafiz= character("Hafiz",color="#8fdcff")
define salma= character("Salma", color="#ffb25a")
define yossif= character("Yossif",color="#7cc4ff")
define layla = character("Layla",color="#c79bff")
define karem= character("Karem", color="#ff8a8a")
define nour=character("Nour",color="#8affd2")
define mansour=character("Mansour", color="#f0d9a0")
define captain = character ("Captain", color= "#ffd45a")
define engineer=character("Engineer", color="#ff9a55")
define guide = character("Guide", color="#a6e8a6")
define girl= character("Girl", color="#ffd1e8")
define crowd= character("crowd", color="#cccccc")
define flash= fade(0.1,00,0.5, color="#ffffff")

# where the character stand on screen
transform p_left:
    xalign 0.18
    yalign 1.0
    zoom 0.85

transform p_right:
    xalign 0.82
    yalign 1.0
    zoom 0.85

transform p_mid:
    xalign 0.5
    yalign 1.0
    zoom 0.85

# what the player has saved at now
default truth=0
default myth=0
default science=0
default faith=0

# how well the ship holds together

default unity=5

default kept=[]
default erased=[]
default last_pick=""
default record_zero_opened = false
default secret_state="sealed"
default bond_mansour=0
default box_tempered = false
default year=14
default top="trust"

# notes the curators leave for each other

default message_1= ""
default message_2=""
default message_3= ""
default message_4= ""
