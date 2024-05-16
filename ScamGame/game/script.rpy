# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#
#   TODO:
#       - put the choices in capitals / make them shorter
#

define narrator = Character("Narrator", color="#2833a8")
define guide = Character("Scam awareness guy", color="#048c01")

define good_summary = "#048c01"
define bad_summary = "#630c00"

screen buttons():
    imagebutton:
        xalign 0.1
        yalign 0.5
        auto "door_scam_button_%s.png" action [ToggleScreen("buttons"), ToggleScreen("hide_button"), Jump("door_scam_1_start")]

    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "message_scam_button_%s.png" action [ToggleScreen("buttons"), ToggleScreen("hide_button"), Jump("message_scam_1_start")]

    imagebutton:
        xalign 0.9
        yalign 0.5
        auto "phone_scam_button_%s.png" action [ToggleScreen("buttons"), ToggleScreen("hide_button"), Jump("phone_scam_1_start")]

screen scores():

    $ text_money = ""
    $ text_reputation = ""

    frame:
        xpos 30
        ypos 10
        background "score_background.png"

        vbox:

            if money_green:
                $ text_money = "{b}{color=#00ff00}Money: [money]{/color}{/b}"
            else:
                $ text_money = "{b}Money: [money]{/b}"

            if money_show_diff:
                if money_remove:
                    $ text_money = text_money + "{b}{color=#ff0000} (-" + str(money_diff) + "){/color}{/b}"
                else:
                    $ text_money = text_money + "{b}{color=[good_summary]} (+" + str(money_diff) + "){/color}{/b}"

            text _(text_money)

        vbox:
            yalign 0.05

            if reputation_green:
                $ text_reputation = "{b}{color=#00ff00}Reputation: [reputation]{/color}{/b}"
            else:
                $ text_reputation = "{b}Reputation: [reputation]{/b}"

            if reputation_show_diff:
                if reputation_remove:
                    $ text_reputation = text_reputation + "{b}{color=#ff0000} (-" + str(reputation_diff) + "){/color}{/b}"
                else:
                    $ text_reputation = text_reputation + "{b}{color=[good_summary]} (+" + str(reputation_diff) + "){/color}{/b}"

            text _(text_reputation)

    

screen hide_button():

    tag hide_button

    imagebutton:
        xalign 0.95
        yalign 0.8
        auto "hide_button_%s.png" action [HideInterface()]



screen show_summary():

    frame:
        xpos 610
        ypos 50
        background "summary_background.png"

        vbox:
            xmaximum 600
            yalign 0.02
            xalign 0.02
            box_wrap True
            text _("Summary:\n{size=*0.7}" + summary_text + "{/size}")
        

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ money = 20000 # the amount of money
    $ reputation = 5 # your reputation, could be karma as well

    $ money_green = False
    $ reputation_green = False

    $ money_show_diff = False
    $ reputation_show_diff = False

    $ money_diff = 0
    $ reputation_diff = 0

    $ money_remove = False
    $ reputation_remove = False

    $ summary_text = ""

    scene bg white

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
    $ money_show_diff = True
    $ money = 19000
    $ money_diff = 1000
    $ money_remove = True

    narrator "If you were to lose some money in some question, you'll see that the counter shows the amount you lost in red"

    narrator "You'll know something went wrong if that happens."

    $ money_show_diff = False
    $ money = 20000

    narrator "Of course, you'd then let your schizophrenia loose and just say no to everyone trying to contact you, ever."

    $ reputation_green = True

    narrator "Since that's a very quick way to becoming lonely and miserable, you also have the reputation counter."

    narrator "This is a measure of how respectable you are, and correlates with the opinion other people have of you around you."

    $ reputation_green = False
    $ reputation_show_diff = True
    $ reputation_remove = False
    $ reputation_diff = 5
    $ reputation = 10

    narrator "If this is high (8 or more), people will think of you as a nice person!"

    $ reputation_green = False
    $ reputation_show_diff = True
    $ reputation_remove = True
    $ reputation_diff = 9
    $ reputation = 1

    narrator "If it gets too low however (2 or less), people will think you're an asshole."

    $ reputation_show_diff = False
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

    show screen hide_button

    narrator "Finally, you have the hide button on the right."

    narrator "This is useful if you struggle to see what's behind the background. Once you press it, just click once more to go back to the dialog."

    narrator "At the end of each portion of the game, you can expect to see a summary of what went well and what went wrong."

    $ summary_text = """-Click to advance to the next dialog\n{size=*0.3}
{/size}-Sometimes you'll be given a list of options to choose from; click on them\n{size=*0.3}
{/size}-At the top left, you can check your score in terms of money and reputation\n{size=*0.3}
{/size}-At the bottom of the screen is a back button if you want to return to the previous dialog\n{size=*0.3}
{/size}-If you missed any portion of the dialog, you can re-read it under the history button\n{size=*0.3}
{/size}-If you need to see the background more clearly, press the hide button; then click to go back\n{size=*0.3}
{/size}-Summaries such as this one will appear at the end of a segment to tell you how you've done"""
    show screen show_summary()

    narrator "Such as this one. That way, you'll always remember what you did well and what needs improvement."

    hide screen show_summary

    narrator "Well then, good luck!"

    scene bg white_clear

    narrator "You may now choose your gamemode."

    hide screen scores
    hide screen hide_button
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

    $ money = 20000
    $ reputation = 5
    $ summary_text = ""

    show screen scores()

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

    $ summary_text += "-{color=[good_summary]}You didn't trust the fake package{/color}"

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

    $ summary_text += "-{color=[bad_summary]}You fell for a false package delivery notice{/color}"

    narrator "You click the link, and go through the menus on the portal that opens"
    narrator "You realise that the delivery address is wrong, and that you have to pay a fee to correct it"

    $ money_show_diff = True
    $ money_diff = 1000
    $ money -= money_diff
    $ money_remove = True

    narrator "You lose some money."

    $ money_show_diff = False

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

    $ summary_text += "{size=*0.3}\n{/size}-{color=[good_summary]}You identified a fake bank message{/color}"

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

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[bad_summary]}You fell for a fake bank message{/color}"

    narrator "You click the link."

    narrator "It opens a portal asking you for your bank credentials"

    narrator "You enter them to 'fix' the payment info"

    $ money_show_diff = True
    $ money_diff = 4000
    $ money -= money_diff
    $ money_remove = True

    narrator "Some time later, you receive another message from your real bank that a lot of your funds have been transferred to an unknown account."

    narrator "You lose a lot of money."

    $ money_show_diff = False

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

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[good_summary]}You didn't click the weird gift link{/color}"

    scene bg living_room_blur
    with dissolve

    scene bg living_room_guide
    with dissolve
    guide "Hey, you did well spotting that scam!"
    guide "“if it’s too good to be true, it probably is” is an excellent principle to live by on the internet."
    guide "you really want to check if you genuinely did win something, contact the customer service department of the company or business."

    jump message_scam_4_start

label message_scam_3_success2:

    $ summary_text += "\n{size=*0.3}\n{/size}-You didn't put your personal info into the weird gift link, but still clicked it"

    scene bg living_room_guide
    with dissolve

    guide "Hey, good job! You detected the scam!"
    guide "Entering personal information online could be risky."
    guide "It's better to avoid sharing sensitive details with unknown sources."

    jump message_scam_4_start


label message_scam_3_fail:

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[bad_summary]}You entered your personal details into a fake giveaway{/color}"

    narrator "You enter in your personal details to get the free voucher you've won."

    $ money_show_diff = True
    $ money_diff = 1000
    $ money -= money_diff
    $ money_remove = True

    narrator "The website does not seem in any way strange to you."

    $ money_show_diff = False

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

    narrator "You try to be polite by responding that they have the wrong number."

    scene bg living_room_scam4_2_2
    with dissolve

    narrator "Not long after you receive a response."

    menu:
        narrator "You..."

        "Politely say that mistakes happen.":
            jump message_scam_4_2resp_polite

        "Scold them that they should have noticed the error sooner.":
            jump message_scam_4_response_scold

label message_scam_4_2resp_polite:

    scene bg living_room_scam4_2_3
    with dissolve

    $ reputation_show_diff = True
    $ reputation_diff = 1
    $ reputation += reputation_diff
    $ reputation_remove = False

    narrator "You send a polite message that no harm was done."

    $ reputation_show_diff = False

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

    scene bg living_room_scam4_4_1
    with dissolve

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[bad_summary]}You were rude to some stranger although there was no reason to{/color}"

    $ reputation_show_diff = True
    $ reputation_diff = 1
    $ reputation -= reputation_diff
    $ reputation_remove = True

    narrator "You scold them that they should have looked at their info before contacting you."

    $ reputation_show_diff = False

    

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

    $ reputation_show_diff = True
    $ reputation_diff = 1
    $ reputation += reputation_diff
    $ reputation_remove = False

    narrator "You send a polite message that no harm was done."

    $ reputation_show_diff = False

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

    $ reputation_show_diff = True
    $ reputation_diff = 1
    $ reputation -= reputation_diff
    $ reputation_remove = True

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[bad_summary]}You were rude to some stranger although there was no reason to{/color}"

    narrator "You scold them that they should have looked at their info before contacting you."

    $ reputation_show_diff = False

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

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[bad_summary]}You disclosed your real name{/color}"

    narrator "You send them your real name."

    scene bg living_room_scam_4_3_5
    with dissolve

    narrator "You receive a reply from the unknown contact."

    jump message_scam_5_start

label message_scam_4_polite_fake:

    scene bg living_room_scam4_3_6
    with dissolve

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[good_summary]}You didn't disclose your real name{/color}"

    narrator "You send them a fake name."

    scene bg living_room_scam4_3_7

    narrator "You receive a reply from the unknown contact. They don't budge at the fake name."

    jump message_scam_5_start

label message_scam_4_scold_name:

    scene bg living_room_scam4_4_3
    with dissolve

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[bad_summary]}You disclosed your real name{/color}"

    narrator "You send them your real name."

    scene bg living_room_scam4_4_4
    with dissolve

    narrator "You receive a reply from the unknown contact."

    jump message_scam_5_start

label message_scam_4_scold_fake:

    scene bg living_room_scam4_4_5
    with dissolve

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[good_summary]}You didn't disclose your real name{/color}"

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

    $ summary_text += "\n{size=*0.3}\n{/size}-You didn't help the stranger; there's no telling if they were a scammer or not"

    narrator "You refuse and block the number."

    scene bg living_room_guide
    with dissolve

    guide "Good job! Your scam radar is on point. Remember, never trust someone asking for money through chat."
    guide "Always verify requests and never send money to someone you don't know or trust."

    jump message_scam_6_start


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

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[good_summary]}You didn't get scammed by a stranger{/color}"

    narrator "You decide to ignore the request and block the number."

    scene bg living_room_guide
    with dissolve

    guide "Good job! Your scam radar is on point. Remember, never trust someone asking for money through chat."
    guide "Always verify requests and never send money to someone you don't know or trust."

    jump message_scam_6_start

label message_scam_5_inquire_fail:

    scene bg living_room_blur
    with dissolve

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[bad_summary]}You got scammed by a stranger, for good or for ill{/color}"

    $ money_show_diff = True
    $ money_diff = 1000
    $ money -= money_diff
    $ money_remove = True

    narrator "You send the money to the account given to you."

    $ money_show_diff = False

    scene bg living_room_guide
    with dissolve

    guide "Uh-oh! Looks like you've been taken for a ride!"
    guide "Remember, while it's great to be generous and helpful, always verify requests for money, especially online, you should never trust someone that asks you money by chat."

    jump message_scam_6_start


### MESSAGE SCAM 6
label message_scam_6_start:

    scene bg living_room_blur
    with dissolve

    narrator "You received one final message from an unknown sender."

    scene bg living_room_scam6
    with dissolve

    menu:
        narrator "You..."

        "Send a donation":
            jump message_scam_6_fail

        "Do nothing and block the number":
            jump message_scam_6_success


label message_scam_6_success:

    scene bg living_room_blur
    with dissolve

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[good_summary]}You didn't get scammed by a fake charity{/color}"

    narrator "You ignore the request and block the number."

    scene bg living_room_guide
    with dissolve

    guide "Hey, you did well not donating anything!"
    guide "It's rare that unsollicited calls for charity are not a scam."
    guide "For instance, this 'sunshine charity' may only be a fake company name for a scammer."
    guide "If you want to donate money, contact charities directly."

    jump scam_end


label message_scam_6_fail:

    scene bg living_room_blur
    with dissolve

    $ summary_text += "\n{size=*0.3}\n{/size}-{color=[bad_summary]}You got scammed by a fake charity{/color}"

    narrator "You go through the process of donating money to this 'Sunshine Charity'."

    $ money_show_diff = True
    $ money_diff = 1000
    $ money -= money_diff
    $ money_remove = True

    narrator "You lose some money."

    $ money_show_diff = False

    scene bg living_room_guide
    with dissolve

    guide "Oh no! You got scammed."
    guide "Scammers may use evil tactics like registering a fake company name to appear as a charity."
    guide "There's no way to know for sure that such a charity like the 'Sunshine Charity' actually is legitimate."
    guide "If you want to donate money, you should contact charities directly."

    jump scam_end



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


label scam_end:

    scene bg white_clear
    with dissolve

    narrator "You're at the end of this portion of the game."

    show screen show_summary()

    narrator "Here's how you did"

    hide screen show_summary

    narrator "You will now return to the menu."

    hide screen scores

    call screen buttons()
