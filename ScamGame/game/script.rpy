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

screen scores():

    $ text_out = ""

    vbox:
        xalign 0.05
        yalign 0.05

        if money_green:
            $ text_out = "{b}{color=#00ff00}Money: [money]{/color}{/b}"
        elif money_red:
            $ text_out = "{b}{color=#ff0000}Money: [money]{/color}{/b}"
        else:
            $ text_out = "{b}Money: [money]"

        if reputation_green:
            $ text_out = text_out + "{b} | {color=#00ff00}Reputation: [reputation]{/color}{/b}"
        elif reputation_red:
            $ text_out = text_out + "{b} | {color=#ff0000}Reputation: [reputation]{/color}{/b}"
        else:
            $ text_out = text_out + "{b} | Reputation: [reputation]{/b}"

        text _(text_out)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ money = 20000 # the amount of money
    $ reputation = 5 # your reputation, could be karma as well

    $ money_green = False
    $ reputation_green = False

    $ money_red = False
    $ reputation_red = False

    scene black

    narrator "Hello! This is your narrator speaking. I'll be helping you along the game. (click to continue)"


    narrator "First, I'll have to explain to you a basic mechanic here, and that is how to win."

    narrator "Since the goal of this game is to not get scammed, you get two metrics that tell you how you're doing."

    show screen scores()

    narrator "That's why you get two scores."

    $ money_green = True

    narrator "The first one is your money counter. You start out with a respectable amount of money."

    narrator "It should be fairly obvious to you that you don't want to lose money."

    narrator "If you do, please send it to CH81 0027 2272 1468 6540 T with the payment description as \"Gullibility tax\"."

    $ money_green = False
    $ money_red = True

    narrator "If you were to lose some money in some question, you'll see that the counter becomes red."

    narrator "You'll know something went wrong if that happens."

    $ money_red = False

    narrator "Of course, you'd then let your schizophrenia loose and just say no to everyone trying to contact you, ever."

    $ reputation_green = True

    narrator "Since that's a very quick way to becoming lonely and miserable, you also have the reputation counter."

    narrator "This is a measure of how respectable you are, and correlates with the opinion other people have of you around you."

    $ reputation = 10

    narrator "If this is high (8 or more), people will think of you as a nice person!"

    $ reputation_green = False
    $ reputation_red = True
    $ reputation = 1

    narrator "If it gets too low however (2 or less), people will think you're an asshole."

    $ reputation_red = False
    $ reputation = 5

    narrator "So remember to be wary, but also not too paranoid to the point where it may seem rude."

    narrator "For the rest of the game, dialogs will carry the same format as what you're seeing right now."

    narrator "Occasionally you'll get to make some choices."
    
    menu:
        narrator "At that moment, buttons such as these will appear; you can click on them to make your choice"

        "Choice 1":
            $ reputation_green = False

        "Choice 2":
            $ reputation_green = False

    narrator "If for some reason you skipped a question, you can always hit the \"Back\" button at the bottom of the screen."

    narrator "And if you forgot what has previously been said, you can hit the \"History\" button to get a recap on what happened."

    narrator "Finally, if you hit the H key on your keyboard, you can hide the dialog to get a better look at the background. Remember this trick well!"

    narrator "Well then, good luck!"

    narrator "You may now choose your gamemode."

    call screen buttons()

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

# ----------------------------------------
#             MESSAGE SCAMS
# ----------------------------------------


### SCAM 1

label message_scam_1_start:

    scene bg living_room
    with fade

    narrator "You are sitting in your living room"

    scene bg living_room_blur
    with dissolve
    

    narrator "You check your messages"

    scene bg living_room_scam1
    with dissolve
    narrator "You received a message from an unknown number."

    menu:
        narrator "You..."

        "Block the number":
            jump message_scam_1_success

        "Click the link":
            jump message_scam_1_fail

label message_scam_1_success:
    scene bg living_room_blur
    with dissolve

    narrator "You block the number."
    scene bg living_room_guide
    with dissolve

    guide "Hey, you did well blocking that number!"
    

    guide "Never trust links that don't contain well-known names such as the Swiss Post, and watch for the spelling"

    guide "Especially if you didn't order any package or the tracking number does not match"

    jump message_scam_2_start


label message_scam_1_fail:

    scene bg living_room_blur
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


### SCAM 2

label message_scam_2_start:

    scene bg living_room_blur
    with dissolve

    scene bg living_room_scam2
    with dissolve
    narrator "You received another message from an unknown number."

    menu:
        narrator "You..."

        "Block the number":
            jump message_scam_2_success

        "Click the link":
            jump message_scam_2_fail

label message_scam_2_success:
    scene bg living_room_blur
    with dissolve

    narrator "You block the number."

    scene bg living_room_guide
    with dissolve

    guide "Hey, you did well blocking that number!"

    guide "Banks will never ask you directly for your credentials, especially not through a website that does not have the name of the bank in it"

    guide "Be very wary of such types of messages!"

    jump message_scam_3_start

label message_scam_2_fail:


    scene bg living_room_blur
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

    jump message_scam_3_start


# SCAM 3

label message_scam_3_start:

    scene bg living_room_blur
    with dissolve

    scene bg living_room_scam3_1
    with dissolve
    narrator "You received another message from an unknown number."

    menu:
        narrator "You..."

        "Click the link to claim the voucher.":
            jump message_scam_3_cont

        "Ignore the message.":
            jump message_scam_3_success1

label message_scam_3_cont:

    scene bg living_room_scam3_2
    with dissolve
    narrator "A website pops open, prompting you to enter your credentials."

    menu:
        narrator "You..."

        "Put your info in":
            jump message_scam_3_fail

        "Close the website":
            jump message_scam_3_success2

label message_scam_3_success1:

    scene bg living_room_blur
    with dissolve

    scene bg living_room_guide
    with dissolve
    guide "Hey, you did well spotting that scam!"
    guide "“if it’s too good to be true, it probably is” is an excellent principle to live by on the internet."
    guide "you really want to check if you genuinely did win something, contact the customer service department of the company or business."

    jump message_scam_4_start

label message_scam_3_success2:

    scene bg living_room_blur
    with dissolve

    guide "Hey, good job! You detected the scam!"
    guide "Entering personal information online could be risky."
    guide "It's better to avoid sharing sensitive details with unknown sources."

    jump message_scam_4_start


label message_scam_3_fail:

    narrator "You enter in your personal details to get the free voucher you've won."
    narrator "The website does not seem in any way strange to you."

    scene bg living_room_guide
    with dissolve

    guide "Hey, you got scammed!"
    guide "Entering personal information online could be risky."
    guide "“if it’s too good to be true, it probably is” is an excellent principle to live by on the internet."
    guide "you really want to check if you genuinely did win something, contact the customer service department of the company or business."

    jump message_scam_4_start


### SCAM 4

label message_scam_4_start:

    scene bg living_room_blur
    with dissolve

    narrator "You received a message from what looks like someone with the wrong number."

    scene bg living_room_scam4_1
    with dissolve

    narrator "You think about how to react to this."

    menu:
        narrator "You..."

        "Send a message telling them that you're not Mike":
            jump message_scam_4_response

        "Don't respond.":
            jump message_scam_4_ghost


label message_scam_4_response:

    scene bg living_room_scam4_2_1
    with dissolve

    narrator "You try to be polite by responding that they have the wrong number. "

    scene bg living_room_scam4_2_2
    with dissolve

    narrator "Not long after you receive a response."

    menu:
        narrator "You..."

        "Politely say that mistakes happen.":
            jump message_scam_4_2resp_polite

        "Scold them that they should have noticed the error sooner.":
            jump message_scam_4_2resp_scold

label message_scam_4_2resp_polite:

    scene bg living_room_scam4_X
    with dissolve

    narrator "You send a polite message that no harm was done."

    scene bg living_room_scam4_3_3
    with dissolve

    narrator "You receive another message asking for your name."

    menu:
        narrator "You..."

        "Send your real name":
            jump message_scam_4_polite_name

        "Send a fake name":
            jump message_scam_4_polite_fake

label message_scam_4_2resp_scold:

label message_scam_4_ghost:

    narrator "You decide to not respond."

    scene bg living_room_scam4_3_1
    with dissolve

    narrator "Not long after, you receive a new message from the same sender."

    menu:
        narrator "You..."

        "Politely say that mistakes happen.":
            jump message_scam_4_response_polite

        "Scold them that they should have noticed the error sooner.":
            jump message_scam_4_response_scold

label message_scam_4_response_polite:

    scene bg living_room_scam4_3_2
    with dissolve

    narrator "You send a polite message that no harm was done."

    scene bg living_room_scam4_3_3
    with dissolve

    narrator "You receive another message asking for your name."

    menu:
        narrator "You..."

        "Send your real name":
            jump message_scam_4_polite_name

        "Send a fake name":
            jump message_scam_4_polite_fake


label message_scam_4_response_scold:

    scene bg living_room_scam4_4_1
    with dissolve

    narrator "You scold them that they should have looked at their info before contacting you."

    scene bg living_room_scam4_4_2
    with dissolve

    narrator "You receive another message asking for your name."

    menu:
        narrator "You..."

        "Send your real name":
            jump message_scam_4_scold_name

        "Send a fake name":
            jump message_scam_4_scold_fake

label message_scam_4_polite_name:

    scene bg living_room_scam4_3_4
    with dissolve

    narrator "You send them your real name."

    scene bg living_room_scam_4_3_5
    with dissolve

    narrator "You receive a reply from the unknown contact."

    jump message_scam_5_start

label message_scam_polite_fake:

    scene bg living_room_scam4_3_6
    with dissolve

    narrator "You send them a fake name."

    scene bg living_room_scam4_3_7

    narrator "You receive a reply from the unknown contact. They don't budge at the fake name."

    jump message_scam_5_start

label message_scam_4_scold_name:

    scene bg living_room_scam4_4_3
    with dissolve

    narrator "You send them your real name."

    scene bg living_room_scam4_4_4
    with dissolve

    narrator "You receive a reply from the unknown contact."

    jump message_scam_5_start

label message_scam_4_scold_fake:

    scene bg living_room_scam4_4_5
    with dissolve

    narrator "You send them a fake name."

    scene bg living_room_scam4_4_6
    with dissolve

    narrator "You receive a reply from the unknown contact. They don't react to the obviously fake name."

    jump message_scam_5_start


### SCAM 5 (continuation of 4)
label message_scam_5_start:

    scene bg living_room_scam5_1
    with dissolve

    narrator "After some time, you receive a flurry of messages from the same sender."

    scene bg living_room_scam5_2
    with dissolve

    narrator "It seems that they need help in their unfortunate situation."

    menu:

        narrator "You..."

        "Refuse, you don't know them.":
            jump message_scam_5_refuse

        "Ask them what they need.":
            jump message_scam_5_inquire

label message_scam_5_refuse:

    scene bg living_room_blur
    with dissolve

    narrator "You refuse and block the number."

    scene bg living_room_guide
    with dissolve

    guide "Good job! Your scam radar is on point. Remember, never trust someone asking for money through chat."
    guide "Always verify requests and never send money to someone you don't know or trust."


label message_scam_5_inquire:

    scene bg living_room_scam5_3_2
    with dissolve

    narrator "You ask them what they need."

    scene bg living_room_scam5_3_3
    with dissolve

    narrator "They reply that they need 1000.- as well as their bank details."

    menu:

        narrator "You..."

        "Send the money to the account.":
            jump message_scam_5_inquire_fail

        "Do nothing and block the number.":
            jump message_scam_5_inquire_success


label message_scam_5_inquire_success:

    scene bg living_room_blur
    with dissolve

    narrator "You decide to ignore the request and block the number."

    scene bg living_room_guide
    with dissolve

    guide "Good job! Your scam radar is on point. Remember, never trust someone asking for money through chat."
    guide "Always verify requests and never send money to someone you don't know or trust."

    return

label message_scam_5_inquire_fail:

    scene bg living_room_blur
    with dissolve

    narrator "You send the money to the account given to you."

    scene bg living_room_guide
    with dissolve

    guide "Uh-oh! Looks like you've been taken for a ride!"
    guide "Remember, while it's great to be generous and helpful, always verify requests for money, especially online, you should never trust someone that asks you money by chat."

    return

# ----------------------------------------
#           PHONE SCAMS
# ----------------------------------------

label phone_scam_1_start:

    return


# ----------------------------------------
#           DOOR TO DOOR SCAMS
# ----------------------------------------


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
