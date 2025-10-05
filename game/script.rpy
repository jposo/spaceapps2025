# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Stella")

transform shake:
    linear 0.05 xoffset -5 yoffset -5
    linear 0.05 xoffset 5 yoffset 5
    linear 0.05 xoffset -5 yoffset 5
    linear 0.05 xoffset 5 yoffset -5
    linear 0.05 xoffset -5 yoffset -5
    linear 0.05 xoffset 5 yoffset 5
    linear 0.05 xoffset 0 yoffset 0

transform left_center: # I've renamed it for clarity
    xalign 0.1
    yalign 0.5  # 0.5 = Vertical Center

label start:
    scene bg sun1 at truecenter
    with fade

    "In the heart of a star, the surface is never still."
    "Tides of fire rise and fall."
    "Here, where the light never sleeps, something is about to awaken..."

    "In this cooler region of the Sun, magnetic fields get tangled like invisible threads."

    show bg sun2 at truecenter:
        ease 0.5 zoom 1.15

    "Above the Sun lives its corona: an atmosphere of glowing gas and particles that travel faster than the wind."
    "Sometimes, the tension grows… and something extraordinary happens."

    show bg sun3 at truecenter:
        ease 0.5 zoom 1.3

    "Here, energy transforms into brilliant flashes, waves, and eruptions."

    show bg sun4 at truecenter:
        ease 0.5 zoom 1.45

    window hide
    camera at shake
    pause 1.5

    show stella nervous at truecenter
    s "...Hello?"

    menu:
        "Return":
            show stella lockedin at truecenter
            s "I'm scared, I'll just stay here..."
            scene black with fade
            return
        "Explore":
            pass
    
    show stella lockedin at truecenter
    s "I'm alive, and I'm... floating?! What am I?"

    show stella derp at truecenter
    s "Whatever, this is awesome!"

    show stella happy at truecenter
    s "Wheeee!"

    show stella happy at offscreenright
    with move


    scene bg space at truecenter
    with fade

    s "Caca"

    return
