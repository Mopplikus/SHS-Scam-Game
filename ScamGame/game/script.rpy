# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("Narrator")
define guide = Character("Scam awareness guy", color="#ffe600")

screen buttons():
    imagebutton:
        xalign 0.1
        yalign 0.5
        auto "door_scam_button_%s.png" action [ToggleScreen("buttons"), Jump("door_scam_1_start")]

    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "message_scam_button_%s.png" action [ToggleScreen("buttons"), Jump("message_scam_1_start")]

    imagebutton:
        xalign 0.9
        yalign 0.5
        auto "phone_scam_button_%s.png" action [ToggleScreen("buttons"), Jump("phone_scam_1_start")]

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




label message_scam_1_start:

    narrator "You are sitting in your living room"

    scene bg living_room
    with fade

    narrator "You check your messages"

    scene bg message_scam_1
    with dissolve
    narrator "You received a message from an unknown number."

    menu:
        narrator "You..."

        "Block the number":
            jump message_scam_1_success

        "Click the link":
            jump message_scam_1_fail

label message_scam_1_success:
    scene bg living_room
    with dissolve

    narrator "You block the number."
    scene bg living_room_guide
    with dissolve

    guide "Hey, you did well blocking that number!"
    

    guide "Never trust links that don't contain well-known names such as the Swiss Post, and watch for the spelling"

    guide "Especially if you didn't order any package or the tracking number does not match"

    jump message_scam_2_start


label message_scam_1_fail:

    scene bg living_room
    with dissolve

    narrator "You click the link, and go through the menus on the portal that opens"
    narrator "You realise that the delivery address is wrong, and that you have to pay a fee to correct it"
    narrator "You lose some money."

    scene bg living_room_guide
    with dissolve

    guide "Hey, you got scammed!"
    guide "Never trust links that don't contain well-known names such as the Swiss Post, and watch for the spelling"
    guide "Especially if you didn't order any package or the tracking number does not match"
    guide "Better luck next time!"

    jump message_scam_2_start


label message_scam_2_start:

    scene bg living_room
    with dissolve

    scene bg message_scam_2
    narrator "You received another message from an unknown number."

    menu:
        narrator "You..."

        "Block the number":
            jump message_scam_2_success

        "Click the link":
            jump message_scam_2_fail

label message_scam_2_success:
    scene bg living_room
    with dissolve

    narrator "You block the number."

    scene bg living_room_guide
    with dissolve

    guide "Hey, you did well blocking that number!"

    guide "Banks will never ask you directly for your credentials, especially not through a website that does not have the name of the bank in it"

    guide "Be very wary of such types of messages!"

    return

label message_scam_2_fail:


    scene bg living_room
    with dissolve

    narrator "You click the link."

    narrator "It opens a portal asking you for your bank credentials"

    narrator "You enter them to 'fix' the payment info"

    narrator "Some time later, you receive another message from your real bank that a lot of your funds have been transferred to an unknown account."

    narrator "You lose a lot of money."

    scene bg living_room_guide
    with dissolve
    guide "Hey, you got scammed!"
    guide "Banks will never ask you directly for your credentials, especially not through a website that does not have the name of the bank in it"
    guide "Be very wary of such types of messages, because there's no telling in what they'll do with your bank account!"
    guide "Better luck next time"

    return


label phone_scam_1_start:

    return

label door_scam_1_start:

    return

    
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
