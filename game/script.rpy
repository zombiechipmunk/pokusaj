﻿# You can place the script of your game in this file.

    # Set up the size of the screen, and the window title.


define e = Character('Lucy', color="#FFC0CB")
define r = Character('Roland', color= "#8B2500")
define l = Character("Louis", color = "#0000CD")
define j = Character("Jeremy", color = "#00BFFF")
init:
    $ r_relationship = 0
    $ l_relationship = 0
    $ j_relationship = 0
image bg space = "110530.jpg"
image bg room = "120529.jpg"
image bg classroom = "Classroom_01_day.jpg"
image bg school_corridor_afternoon = "school_corridor_afternoon.jpg"
image Lucy normal= im.Scale("Default.png", 200, 500)
image Roland normal = im.Scale("MS2-smile1.png", 200, 600)
image Lucy sweat1 = im.Scale("sweat1.png",200,500)
image Roland flirty = im.Scale("MS2-wink2.png", 200, 600)
image Lucy scared1 = im.Scale("scared1.png",200,500)
image Lucy shock1 = im.Scale("shock1.png",200,500)
image Lucy shy = im.Scale("embarrassed2.png",200,500)
image Lucy pout = im.Scale("pout1.png",200,500)
image Lucy happy1 = im.Scale("smile3.png",200,500)
image Lucy happy2 = im.Scale("smile1.png",200,500)
image Louis flirty = im.Scale("MS1-wink.png",300,600)
image Louis normal = im.Scale("MS1-default.png",300,600)
image Roland happy = im.Scale("MS2-smile6.png",200,600)
image Roland upset = im.Scale("MS2-upset1.png",200,600)
image Louis upset = im.Scale("MS1-awkward.png",300,600)
image Louis unhappy = im.Scale("MS1-pout.png",300,600)
image Roland sad = im.Scale("MS2-sad.png",200,600)
image Lucy tired = im.Scale("huh1.png",200, 500)
image Jeremy surprised = im.Scale("MS3-surprised2.png",200,600)
image Jeremy smile = im.Scale("MS3-smile5.png", 200, 600)





# The game starts here.
label start:
    play music "Intro.mp3" fadeout 1
    queue music "Intro.mp3"
    scene bg space
    with fade

    e "Aristophanes believed that humans originally had four legs, four arms and one head with two faces."
    e "He believed, that existing as such, they were strong enough to pose a threat even for the Gods."
    e "Because of it, the Gods were distressed. They could not simply get rid of them- They loved their sacrifices."
    e "So, Zeus came to a solution, a brilliant one, indeed."
    e "He split them in half to weaken them, thus condemning the humans to isolation and endless longing for their other half."
    e "So, the halves were soulmates. Perfect together."
    e "Separated, they were in pain."
    e "Love was cruel to the Greeks,"
    e "Cupid and Psyche, Orpheus and Eurydice, they were all soulmates forced to part."
    e "Punished by the hands of faith."
    e "Yet, there is a distinct beauty in their suffering."
    e "Imagine, to love so much, everything else seems irrelevant."
    e "I wonder if I will ever be able to find such a beautiful love worth sacrificing for."
    e "I wish, but,as it seems, it is not going to happen."
    stop music fadeout 1
    scene bg classroom
    show Lucy shock1
    with fade
    play music "Forever forward.mp3" fadeout 1
    queue music "Forever forward.mp3" 
    "It is valentines day."
    "And, once again, I am alone."
    "Usually, I am not bothered by my love life- or, better said, lack of love life."
    "But, somehow, surrunded by couples, even in the classroom..."
    "Makes me feel really lonely."
    "?""Why so glum, sugar plum?"
    show Roland flirty at left
    show Lucy shy
    "Roland appears and winks, I can feel blood rushing to my head."
    "Roland, Louis and I used to be best friends."
    "But, suddenly, they got in a fight, and after that Roland started avoiding me."
    "I tried to ask them what happened, but neither would answer."
    e "Roland! W-what's going on?"
    show Roland normal at left
    r "Nothing? I'm just curious about why you seem down today. You've been moping the whole first period"
    show Lucy shock1
    "I didn't think he would notice- after all, Roland and I have stopped hanging out years ago."
    "This means he has been watching me whole period? What is going on?"
    show Lucy scared1
    "I miss him, I miss the trio we made. Maybe-just maybe the two of them made up and he's trying to gather the gang once again?"
    "But, maybe he got into a nother fight with Louis, and is trying to prove a point or something."
    "We all know Louis has a soft spot for me, and I don't want to get in the middle of their ongoing war."
    "If I tell him... Maybe we could be friends again..."
    "Or... Louis could have one of his jealousy tantrums again..."
    menu:
        "Just tell him- no real harm done.":
            jump Roland
        "Better not - why risk it?":
            jump Louis
    stop music fadeout 1
            
    return
label Roland:
    scene bg classroom
    show Lucy normal
    show Roland normal at left
    "Even if Louis gets jealous, for what there is no need, I can just ignore hime."
    "After third period, he'll get over it."
    e "Well, nothing really, just, I can't help feeling jealous of all the couples."
    e "I mean... It's valentines day, and I fell a little left out."
    show Roland flirty at left
    r "Oh, you have a crush? What's he like?"
    show Lucy shy
    e "No I don't! I knew you'd just tease me"
    show Lucy pout
    e "I shouldn't have told you."
    r "Ohh, don't be like that, you're cute when you're upset"
    show Lucy shy
    e "W-what?"
    show Roland happy at left
    r "Now you're even cuter!"
    r "If you continue being so cute..."
    show Roland flirty at left
    r "I might try to steal you"
    r "After all, I am rather fond of cute things"
    "?""Yo, Roland, what are you doing to our poor Lucy?"
    show Lucy happy1
    with None
    show Louis flirty at right
    with dissolve
    l "Is he bothering you, love?"
    show Lucy happy2
    e "No! Maybe teasing a bit, but I don't mind."
    show Louis unhappy at right
    l "Really?"
    show Roland normal at left
    r "Yes, Louis."
    show Louis upset at right
    l "Oh..."
    l "I have to go, see you Lucy, darling!"
    hide Louis upset
    with moveoutleft
    show Lucy shock1
    e "What the-?"
    r "Well, We dont get along very well"
    e "I know, but this is odd behaviour, even for Louis!"
    e "And, you might as well tell me why you got into that stupid fight."
    r "Well, we just didn't agree on a solution to a problem. It doesn't matter."
    "*bell rings*"
    show Roland flirty at right
    r "See you later, alligator."
    show Lucy happy1
    e"see you in a while, crocodile"
    hide bg classroom
    hide Roland flirty
    hide Lucy happy
    with dissolve
    $ r_relationship += 1
    
    jump continue
    return
label Louis:
    scene bg classroom
    show Lucy  scared1
    show Roland normal at left
    "Better not to risk it, Louis can be very tiring when jealous."
    
    e "No, its really nothing, I just havent had enough sleep."
    "?" "Yo, Roland, stop bothering out poor Lucy"
    show Lucy happy1
    show Roland sad at left
    e "Louis!"
    show Louis flirty at right
    show Lucy happy2
    e "How are you!"
    l "Im fine, you? Been up to no good, as usual?"
    show Roland upset at left
    r"Err... I have to go, see you!"
    hide Roland upset
    with moveoutright
    show Lucy shock1
    e "What the-?"
    show Louis normal at right
    l "We dont get along very well."
    e "Well, I know, but neither of you bothered on telling me why!"    
    l "Well... We both liked the same things, but there was one thing we liked too much to share."
    l "We couldnt agree on the sollution of the issue, ending in a fight."
    show Louis flirty at right
    l "I won."
    show Louis normal at right
    l "It seems, though, that he isnt holding on his end of the bargain."
    e" How come you didn't tell me earlier? Even now you are being awfully vague."
    e "I deserve to know- You ARE my best friend."
    e "And Roland and I used to be close."
    l "We didn't really talk about it."
    l "It isnt a well known issue."
    show Lucy pout
    e " Though it is too bad you dont get along"
    l "I guess..."
    "*bell rings*"
    e"Ugh, we better get seated."


    hide bg classroom
    hide Lucy pout
    hide Louis normal
    with dissolve
    $ l_relationship += 1
    
    jump continue
    
    
    return
label continue:
    scene bg school_corridor_afternoon
    show Lucy tired
    with dissolve
    "Thoroughly hungry and craving, no, desperately needing a cup of coffee, I aimelessly began wandering through the school corriddors."
    "I could feel my heavy eyelids closing as I struggled to remain awake."
    "*CRASH*"
    show Jeremy surprised at right
    with vpunch
    j "Hey! Are you all right?"
    show Lucy scared1
    e "Yeah, I guess I am... How are you? I am so sorry!"
    show Jeremy smile at right
    j "No, don't be, all is well that ends well!"
    "He said beaming at me, the fog that clouded my thought finally lifted."
    show Lucy shy
    "He had the bluest eyes, I could feel my heartbeat rising as I realised our close proximity."
    e "So... Pretty..."
    "I hear myself mutter, and  the moment I realise what just happened."
    show Lucy shock1
    e "Eh, sorry, I have to go, I have to... I know that..."
    e "EEEEH!"
    hide Lucy shock 1
    with moveoutleft
    
    
    
    
    return

    
    