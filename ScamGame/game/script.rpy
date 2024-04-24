# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("Narrator")
define salesman = Character("Salesman", color="#00cc00")

screen buttons():
    imagebutton:
        xalign 0.2
        yalign 0.5
        auto "button1_%s.png" action [ToggleScreen("buttons"), Jump("begin")]

    imagebutton:
        xalign 0.8
        yalign 0.5
        auto "button2_%s.png" action [ToggleScreen("buttons"), Jump("begin")]

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    call screen buttons()

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
label begin:

    narrator "Welcome to the scam guessing game"
    narrator "This is still in development, so don't be afraid to give feedback!"
    
    scene bg porch
    with fade

    narrator "You're walking to your house when you meet an unexpected figure"

    show salesman
    with dissolve

    salesman "Hello! I'm a representative of your state's building inspection department"

    salesman "Your house looks like a fire hazard. You have to buy my insurance for 10'000 CHF or you'll be in legal trouble for sure!"

    menu:
        narrator "You..."

        "Pay him the 10'000CHF you just got from the bank":
            jump oops

        "Flip him off":
            jump win


label oops:

    salesman "Thank you very much! It was a pleasure doing business with you!"

    hide salesman
    with dissolve

    narrator "You get the feeling you shouldn't have trusted him so easily"

    scene bg room
    with fade
    narrator "The end, for now"

    return


label win:

    narrator "You tell the weird man to go fuck himself."

    salesman "Argh! You old people, always know when something's up!"

    hide salesman
    with dissolve

    narrator "You've done well spotting this scam"

    scene bg room
    with fade
    narrator "The end, for now"

    return
