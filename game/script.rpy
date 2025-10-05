init python:
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/low_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/mid_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/high_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

define s = Character("Stella", color="#dc6945", callback=high_beep)
define c = Character("Chronos", color="#c8eeff", callback=mid_beep)
define o = Character("Orbit", color="#827da0", callback=mid_beep)
define echo = Character("The Echo of the Sun", color="#f5c468", callback=low_beep)

transform shake:
    linear 0.05 xoffset -5 yoffset -5
    linear 0.05 xoffset 5 yoffset 5
    linear 0.05 xoffset -5 yoffset 5
    linear 0.05 xoffset 5 yoffset -5
    linear 0.05 xoffset -5 yoffset -5
    linear 0.05 xoffset 5 yoffset 5
    linear 0.05 xoffset 0 yoffset 0

transform longer_shake:
    shake
    shake

transform left_center:
    xalign 0.1
    yalign 0.5

transform right_center:
    xalign 0.9
    yalign 0.5

transform offscreen_topright:
    xalign 1.5
    yalign 0.0

transform offscreen_topleft:
    xalign -0.5
    yalign 0.0

transform offscreen_right_center:
    xalign 1.5
    yalign 0.5

transform pan_background:
    xalign 0.0
    ease 5.0 xalign 1.0

transform pan_background_left:
    xalign 1.5
    ease 5.0 xalign 0.9

transform left_center_no_offset:
    xalign 0.0
    yalign 0.5

image cronos idle:
    "cronos idle1.png"
    linear 0.5 yoffset -10
    0.5
    "cronos idle2.png"
    linear 0.5 yoffset 0
    0.5
    repeat

image bg sun:
    "bg sun1.png"
    0.5
    "bg sun2.png"
    0.5
    "bg sun3.png"
    0.5
    "bg sun4.png"
    0.5
    "bg sun5.png"
    0.5
    repeat

image earth animated:
    "earth/earth000.png"
    0.5
    "earth/earth010.png"
    0.5
    "earth/earth020.png"
    0.5
    "earth/earth030.png"
    0.5
    "earth/earth040.png"
    0.5
    "earth/earth050.png"
    0.5
    "earth/earth060.png"
    0.5
    "earth/earth070.png"
    0.5
    "earth/earth080.png"
    0.5
    "earth/earth090.png"
    0.5
    repeat

image stella happy:
    "stella happy.png"
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat

image stella confused:
    "stella confused.png"
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat

image stella derp:
    "stella confused.png"
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat

image stella sugoi:
    "stella sugoi.png"
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat

image stella lockedin:
    "stella lockedin.png"
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat

image stella nervous:
    "stella nervous.png"
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat

image stella venom:
    "stella venom1.png"
    0.5
    "stella venom2.png"
    0.5
    repeat

image orbit huh:
    "orbit huh.png"
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat

image orbit happy:
    "orbit happy.png"
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat

image orbit sad:
    "orbit sad.png"
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat

image orbit meh:
    "orbit meh.png"
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat

image earth static = "earth/earth047.png"

label start:
    label birth:
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

        show stella confused at truecenter
        s "What... am I?"

        "And so, with no destination, a spark of energy was born in the heart of the Sun. Small. Bright. Restless."

        # show stella happy at offscreenright
        # with move

        show stella lockedin at left_center
        s "Everything moves... everything glows… but what am I in the middle of all this?"
        s "Is this... home?"

        show stella nervous at truecenter
        s "I feel like I should go... outward... but... what is out there?"
        
        menu:
            "Try to understand the environment":
                "The Sun is intensely hot, but the gas here in the corona is even hotter — millions of degrees!"
                "This heat makes the plasma so active."
                "The magnetic fields are the real rulers here; they hold the hot gas in place, creating those giant looping shapes you see!"

                show stella lockedin at left_center
                s "The invisible lines are guiding the fire! But they're so tangled. If they break... I bet something big will happen!"
            "Follow the current of energy":
                show stella derp at left_center
                s "It’s too much to think about! I'll just ride the wave and see where it goes!"
                "Stella is caught in the Solar Wind—a constant, fast-moving stream of tiny particles flying away from the Sun."
                "Every second, the Sun launches billions of particles out into space. This is what fills the solar system!"

                show stella nervous at left_center
                s "Wow! This is fast! I feel like I'm finally moving. But... the lines are getting tighter... it’s going to snap!"

        "The tension breaks. The snap is sudden, powerful, and total."
        "Stella is no longer just a spark. She is part of a Coronal Mass Ejection!"

        show stella happy at left_center
        s "I’m flying! I’m finally moving! Wait… where am I going so fast?!"
        show stella happy at offscreenright
        with move

    label travel:
        scene bg space at truecenter
        with fade

        show stella happy at offscreen_topleft

        "Stella was flying faster than she could comprehend. No longer a mere spark, she was a wave, a plume of hot, magnetized gas—a Coronal Mass Ejection—catapulted into the void."
        show stella happy at truecenter
        with move
        s "So many stars! They’re not just tiny specks… they’re everywhere! I never knew the darkness was so wide."
        "She was traveling across the Interplanetary Medium, the vast ocean of space between planets. For a star-born entity, this journey was fast. She was moving at millions of miles per hour, but the distance was still immense."
        "Stella is traveling through the Solar Wind, which acts like a highway for her energy, helping her maintain speed."

        show stella nervous at truecenter
        s "I can’t stop! I keep getting faster. I don’t understand. I just want to… settle."
        "Stella was realizing a crucial, difficult truth: the energy that birthed her now controlled her direction. She was a runaway storm, not a gentle breeze."

        menu:
            "Embrace the power, enjoy the speed.":
                show stella happy at truecenter
                s "This is what I am! If I can't stop, I'll just go faster! Let the energy take me!"
            "Seek understanding, find someone who knows.":
                show stella lockedin at truecenter
                s "I was born here, but I don't belong here yet. I need a guide. There must be other things out here..."

        show stella nervous at truecenter
        s "Whoa! You're… so long! And so slow! Are you a moving star? Are you lost?"

        show stella happy at left_center
        with move
        show cronos idle at right_center:
            zoom 0.5
            nearest True
        c "I am no star, little spark. I am just a wanderer, made of ice and ancient stories. You, however… you are quite new. And quite fast."

        show stella confused at left_center
        s "I don't know what I am! I just snapped out of the Sun and now I can't stop. Do you know what this energy is? It feels like fire, but it looks like light."
        c "Ah, you are an echo of the Sun’s own heartbeat. I've felt the rush of your siblings before, traveling toward the inner worlds. You, child, are a Coronal Mass Ejection. A CME."

        c "You are not just light. You are a bubble of the Sun's plasma—gas so hot its atoms have been stripped bare—carrying with you a powerful magnetic field."
        c "That's why you can't stop; your energy is pushing you forward. You are an electromagnetic storm."
        show stella nervous at left_center
        s "A storm? That sounds… destructive."
        c "Destructive? Perhaps. But a storm is also a change. The question is, what will you do with your power? That energy is you. It can sculpt the space you travel through, or it can shatter the silence."

        c "See that speck ahead? That blue, beautiful sphere? That is your destination. A place called Earth. It is a world of water, life, and a complex shield waiting for you."
        show stella sugoi at left_center
        s "It's… blue. So gentle. I’ve only ever known gold and black. Will I hurt it?"

        c "That is the question you must carry, Stella. Your magnetic field is about to meet theirs. Your choice—your identity—will determine whether you bring light, or darkness."

        show cronos idle at offscreen_right_center:
            zoom 0.5
            nearest True
        with move

        "Stella was no longer an unknown spark. She was a CME, and she was fast approaching the world of humanity. The blue marble waited."


    label earth:
        scene bg space at truecenter
        with fade

        show earth animated at right:
            zoom 10
            nearest True

        "After a journey spanning millions of miles, Stella had arrived."
        "Ahead of her pulsed Earth's invisible shield, its magnetosphere—a powerful magnetic defense, built over eons to protect the fragile life within."
        "This field was an echo of her own power, yet it was fixed and ancient, while she was a violent, moving storm."

        show stella sugoi at topleft

        s "It’s so much... bigger than I imagined. I feel like I'm touching something sacred."
        "She was now in the final, critical space, where her energy would collide with Earth’s own power. There was no going back."

        "Stella feels the twin magnetic pulls of Earth, guiding her down different paths. She must decide where her power will meet the world."
        menu:
            "The Northern Route: Seek the Pole of Light.":
                show orbit happy at topright:
                    zoom 0.5
                    nearest True
                o "Beep. Boop. Incoming stellar energy detected. Hello, Stella. I am Orbit. Please… can you hear me? You are beautiful, but too strong for this space."
                show stella nervous at topleft
                s "A voice! You are so small. Are you what those blue lights built? I… I can’t slow down, Orbit. I am what I am."
                show orbit huh at topright:
                    zoom 0.5
                    nearest True
                o "Please listen. Your energy is immense. If you continue directly, you will overwhelm us. I will be destroyed—and so will the fragile web of light connecting all the life down there."
                o "Power grids, communication, people’s lives… they all depend on this simple, fragile network."

                show orbit sad at topright:
                    zoom 0.5
                    nearest True
                o "They built me not out of arrogance, but out of curiosity. To look up and understand the stars—including you."
                o "They know nothing of hate; they only seek to connect. We are a fragile bridge to your cosmic world, Stella. Don't break the bridge that seeks to greet you."

                # show orbit meh at offscreen_topright
                # with move
                show stella confused at topleft
                s "(thinking) He doesn’t scold me. He pleads, with awe. I wanted to shine. But power without care... only destroys."

                "Stella makes a conscious choice. Her light momentarily dims as she exerts her will, forcing her magnetic field to bend and scatter."

                "Stella had chosen restraint. Her storm did not crash the Earth’s delicate network; it was channeled, transformed."
                "And from her immense power, a final act of creation bloomed. The sky sang her name—Stella—not in fear, but in light, an unforgettable memory of the star-born energy that came in peace."

                # scene black at truecenter
                # with fade

                scene bg good_ending at truecenter
                with fade

                pause 2.0
                "The end."
                scene black at truecenter
                with fade

            "The Southern Route: Follow the Empty Silence.":
                show stella nervous at topleft
                s "It’s quieter here. No voices. No tiny, fragile lights. Just me and the dark."
                echo "Why do you hesitate, my flare? You were born to burn. They look up and forget the true source. They forget our power."
                echo "You are a gift of pure fire. You are meant to remind them of the Sun’s eternal voice. Shine, brighter than ever. Let the world remember the source."

                show stella confused at topleft
                s "(thinking) He's right. I was born from a snap, not a slow simmer. I am a storm! I don’t need guidance. I am power!"

                "Stella yields to the temptation. She stops holding back, amplifying her magnetic storm with a blinding surge of light."
                "The web of light shattered. The raw, beautiful energy of the Sun struck the fragile human network."
                "Power grids collapsed. Communications went dark. The complex, glittering world below fell into a sudden, deep silence."

                "Even in ruin, her light remained—a ghostly shimmer of faint auroras that danced briefly over the planet, hauntingly beautiful. A memory of what could have been."
                "The song of her brilliance faded quickly... in a world gone dark."

                scene bg space at pan_background
                with fade

                show earth static at pan_background_left:
                    zoom 15
                    nearest True

                show stella venom at left_center_no_offset

                camera at longer_shake
                pause 1.5


                scene black at truecenter
                with fade

                s "I... I didn’t mean to hurt them. I just wanted to be me."

                scene bg bad_ending at truecenter
                with fade

                pause 2.0
                "The end... or a new beginning?"
                scene black at truecenter
                with fade
    return
