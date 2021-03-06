﻿# You can place the script of your game in this file.

    # Set up the size of the screen, and the window title.


init python:
    show_Louis = False
    show_Roland = False
    show_Jeremy = False
    
    def stats_overlay():
        if show_Louis:
            ui.frame(
                xalign = 0.5,
                ypos = 400,)
            ui.vbox(xalign = 0.5)
            ui.text ("Louis's Love points: %d" %Louis_love,
                xalign = 0.5)
            ui.bar(max_love, Louis_love,
                style = "my_bar")
            ui.close()
            
        if show_Roland:
            ui.frame(
                xalign = 0.5, #centered
                ypos = 400,) #400 px Down from the Top
            
            ui.vbox(xalign = 0.5)
            ui.text ("Roland's Love Points: %d" %Roland_love, 
                xalign = 0.5)
            ui.bar(max_love, Roland_love, 
                style="my_bar")
            ui.close()
            
        if show_Jeremy:
            ui.frame(
                xalign = 0.5,
                ypos = 400,)
            ui.vbox(xalign = 0.5)
            ui.text ("Jeremy's Love points: %d" %Jeremy_love,
                xalign = 0.5)
            ui.bar(max_love, Jeremy_love,
                style = "my_bar")
            
            ui.close()
        
    config.overlay_functions.append(stats_overlay)
init -2 python:
    Louis_love = 0
    max_love = 100
    
    Jeremy_love = 0
    max_love = 100
    
    Roland_love = 0
    max_love = 100
    
    movie = 0
    observatorium = 0
    
init -5 python:
    style.my_bar = Style(style.default)
    style.my_bar.xalign = 0.5
    style.my_bar.xmaximum = 315
    style.my_bar.ymaximum = 30
    style.my_bar.left_gutter = 5
    style.my_bar.right_gutter = 5
    
    style.my_bar.left_bar = Frame("errors.png",0,0)
    style.mu_bar.right_bar = Frame("bar_empty.png", 0,0)
    style.my_bar.hover_left_bar = Frame("bar_hover.png",0,0)
    
    style.my_bar.thumb = "thumb.png"
    style.my_bar.thumb_shadow = None
    style.my_bar.thumb_offset = 5
    

define e = Character('Lucy', color="#000000")
define r = Character('Roland', color= "#8B2500")
define l = Character("Louis", color = "#0000CD")
define j = Character("Jeremy", color = "#00BFFF")
image bg cafe = im.Scale("cafe_background_2_by_derpinc-d8k97im.png", 1024,800)
image bg rooftop = "rooftop.png"
image bg space = "110530.jpg"
image bg room = "120529.jpg"
image bg classroom = "Classroom_01_day.jpg"
image bg school_corridor_afternoon = "school_corridor_afternoon.jpg"
image bg station = "station_c.jpg"
image Lucy normal= im.Scale("Default.png", 250, 600)
image Lucy tired = im.Scale("huh1.png",250, 600)
image Lucy sweat1 = im.Scale("sweat1.png",250,600)
image Lucy scared1 = im.Scale("scared1.png",250,600)
image Lucy shock1 = im.Scale("shock1.png",250,600)
image Lucy shy = im.Scale("embarrassed2.png",250,600)
image Lucy pout = im.Scale("pout1.png",250,600)
image Lucy angry = im.Scale("angry4.png",250,600)
image Lucy happy1 = im.Scale("smile3.png",250,600)
image Lucy happy2 = im.Scale("smile1.png",250,600)
image Roland normal = im.Scale("MS2-smile1.png", 250, 700)
image Roland flirty = im.Scale("MS2-wink2.png", 250, 700)
image Roland happy = im.Scale("MS2-smile6.png",250,700)
image Roland upset = im.Scale("MS2-upset1.png",250,700)
image Roland sad = im.Scale("MS2-sad.png",250,700)
image Louis flirty = im.Scale("MS1-wink.png",400,700)
image Louis normal = im.Scale("MS1-default.png",400,700)
image Louis upset = im.Scale("MS1-awkward.png",400,700)
image Louis angry = im.Scale("MS1-angry.png", 400, 700)
image Louis unhappy = im.Scale("MS1-pout.png",400,700)
image Jeremy surprised = im.Scale("MS3-surprised2.png",300,700)
image Jeremy smile = im.Scale("MS3-smile5.png", 300, 700)
image Jeremy normal = im.Scale("MS3-default.png",300,700)
image Jeremy flirty = im.Scale("MS3-wink.png",300,700)
image Jeremy shy1 = im.Scale("MS3-shy1.png",300,700)
image Jeremy sad = im.Scale("MS3-sad1.png",300,700)
image Jeremy angry = im.Scale("MS3-angry3.png",300,700)
image nebula = "nebula.jpg"
image mm_idle = "mm_idle.png"
image mm_hover = "mm_hover.png"
image mm_ground = "mm_idle.png"





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
    $ show_Roland = True
    pause 0.5 
    $ Roland_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Roland = True
    
    $ renpy.pause()
    hide text with dissolve
    $ show_Roland = False
    hide bg classroom
    hide Roland flirty
    hide Lucy happy
    with dissolve
    
    
    jump continue0
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
    $ show_Louis = True
    pause 0.5 
    $ Louis_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Louis = True
    pause 0.5
    $ renpy.pause()
    hide text with dissolve
    $ show_Louis = False


    hide bg classroom
    hide Lucy pout
    hide Louis normal
    with dissolve    
    jump continue0
    
    
    return
label continue0:
    scene bg school_corridor_afternoon
    show Lucy tired
    "Thoroughly hungry and craving a cup of coffee, I aimelessly began wandering through the school corriddors."
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
    show Jeremy surprised at right
    e "Eh, sorry, I have to go, I have to... I know that..."
    e "EEEEH!"
    hide Lucy shock 1
    j "What an odd girl..."
    j "Huh?"
    show Jeremy normal at right
    j "A notebook?"
    j "She must've dropped it."
    j "I guess I should return it to her- maybe I can wait after school at the front gates."
    show Jeremy flirty at right
    j "That should be interesting"
    hide Jeremy
    with dissolve
    
    jump station
    return
    
label station:
    scene bg station
    show Lucy tired
    "I basically ran away from the school gates."
    "Dead tired and half asleep, I keep dreaming of coffee ,cheezy romance novels and shoujo mangas."
    "Untill..."
    hide Lucy
    with dissolve
    show Jeremy smile at right
    with dissolve
    show Roland flirty at left
    with dissolve
    show Louis normal
    with dissolve
    "I see them waving at me."
    "They flash me their most charming smiled, but I am definitely in no mood for socializing."
    "But... "
    "Louis always lights up my whole day..."
    "Roland may be trying to fix the friendship I've been missing for years."
    "He was always the comic relief of our group."
    "And Jeremy seems to be holding a very familiar notebook..."
    menu:
        "Ignore them, you're way too tired.":
            jump None
        "Try to get your diary back!":
            jump Jeremy
        "Walk home with Louis-He'll cheer you up.":
            jump Louis1
        "Go to Roland- you've missed him too much":
            jump Roland1
    return
label Jeremy:
    scene bg station
    show Lucy shy
    show Jeremy flirty at right
    e "Hey..."
    e "I'm sorry about earlier."
    j "It's ok hahaha. I'm Jeremy by the way, a senior."
    e "Hi, I'm Lucy, nice too meet you."
    show Lucy happy1
    show Jeremy shy1 at right
    j "Nice to meet you too."
    j "Umm, your notebook... "
    show Lucy shy
    e "Yeah? I gather you have it, am I right?"
    j "Yeah... Here you go."
    show Lucy happy1
    e "Thank you so much."
    show Jeremy flirty at right
    j "No problem"
    j "See you around, I guess."
    e "Sure!"
    $ show_Jeremy = True
    pause 0.5 
    $ Jeremy_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Jeremy = True
    pause 0.5
    $ renpy.pause()
    hide text with dissolve
    $ show_Jeremy = False
    jump continue2
    hide Jeremy flirty
    hide Lucy happy1
    with dissolve
    jump continue2
    
label Louis1:
    scene bg station
    show Lucy happy1
    show Louis flirty at right
    e "Louis! How are you?"
    l "Much better whenever I see you."
    show Lucy shy
    e "Oh you..."
    show Lucy happy2
    e"So what have you been up to?"
    l "Not much."
    l "Though, I have two tickets for the observatorium tomorrow."
    show Louis upset
    l "And I am aware of your obsession with everything celestial."
    show Lucy happy1
    e "I would love to!"
    $ show_Louis = True
    pause 0.5 
    $ Louis_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Louis = True
    pause 0.5
    $ renpy.pause()
    hide text with dissolve
    $ show_Louis = False
    hide Louis flirty
    hide Lucy happy1
    with dissolve
    $observatorium +=1
    
    jump continue2
    return
    
    
label Roland1:
    scene bg station
    show Lucy shy
    show Roland flirty at left
    r "Hey, pretty lady."
    e "Hey Roland, what's up?"
    r "Nothing, just..."
    show Roland normal at left
    r "I have two tickets for the new superhero movie."
    r "You know, the psycho one."
    show Lucy happy2
    e "Really? He's my favourite."
    r "I remeber."
    show Roland flirty at left
    r "So wanna go?"
    show Lucy happy1
    e "Ofcourse!"
    r "I'll pick you up."
    $ show_Roland = True
    pause 0.5 
    $ Roland_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Roland = True
    
    $ renpy.pause()
    hide text with dissolve
    $ show_Roland = False
    hide Roland flirty
    with dissolve
    $movie+=1
    jump continue2
label continue2:
    show bg classroom
    show Lucy tired
    show Louis flirty at left
    e "How do you manage being hyper so early?"
    l "I actually sleep at night. How do you manage being always tired?"
    e "Because I, unlike you, need more than three hours of sleep!"
    e "Waking up to see the alarm set for 6.a.m. drains me of all energy as it is."
    show Lucy sweat1
    e "And we have a test tomorrow..."
    e "The only thing I know is the fact that I know nothing."
    l "It's your fault, by the way."
    l "If you were paying attention, you would have learned."
    show Lucy pout
    e "It is not my fault, really."
    e "I mean, it is..."
    show Lucy normal
    e "Let's not talk about this."
    show Louis normal at left
    l "Ok, ok."
    "Classmate" "Lucy! There's a guy looking for you."
    show Lucy shock1
    show Louis unhappy at left
    e "Who could that be?"
    l "You didn't tell me you have got yourself a boyfriend."
    e "Because I haven't."
    show Louis flirty at left
    l "Oh! Cool!"
    hide Louis flirty
    with dissolve 
    hide Lucy shock1
    with moveoutright
    show Lucy normal
    show Jeremy smile at right
    with dissolve
    e "Oh! Jeremy!"
    j "Hi Lucy!"
    e "How come you're here?"
    j "Been bored. Wanna eat at the rooftop?"
    menu:
        "Sure, why not?":
            jump rooftopJ
        "Can't, I'm staying in the classroom":
            jump classR
        "Can't, I always eat lunch with Louis.":
            jump classL
    hide Jeremy 
    
    return
label rooftopJ:
    show bg rooftop
    show Lucy normal
    show Jeremy normal at right
    e "So, how come you wanted to eat lunch with me?"
    j "No particular reason, just curious about you."
    show Lucy shy
    e "Eeeh, how come?"
    show Jeremy flirty at right
    j "It is not every day I get to meet such a cute girl."
    e "Don't tease me, I'll leave."
    show Jeremy normal at right
    j "Don't leave. I'm just bored there, honest."
    show Lucy normal
    e "Don't you have friends?"
    j "I do- Or I, at least, used to."
    j "I'm getting over a recent break up, and all my friends took her side."
    e "What happened?"
    j "Well, she was going through a rough patch."
    j "I don't even know why I'm telling you about this, but so be it."
    j "I was out in the countryside with my parents."
    show Jeremy sad at right
    j "Her Dad died."
    j "I had no signal whatsoever so I didn't know."
    show Jeremy angry at right
    j "She cheated on me with my older brother who stayed home, because, well, he could."
    j "Anyway, I forgave her, but the next day, I saw them again."
    j "I just couldn't take it- it seemed pointless."
    j "My friends think I was too hard on her."
    show Jeremy normal at right
    e "I don't think so."
    e "I get it, she was having a hard time, and you weren't there for her."
    e "BUT, if she wasn't feeling comfortable with her relationship, she should've tried to talk it over."
    e "If you had stayed with her, both of you would just be suffering, but neither would know for what cause."
    show Jeremy smile at right
    j "Thank you."
    $ show_Jeremy = True
    pause 0.5 
    $ Jeremy_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Jeremy = True
    pause 0.5
    $ renpy.pause()
    hide text with dissolve
    $ show_Jeremy = False
    hide Lucy
    hide Jeremy
    with dissolve
    
    jump corridor
label classR:
    show bg classroom
    show Roland flirty at left
    show Lucy happy1 
    e "Hello there, big boy."
    r "Hey there pretty."
    e "What's a lovely bloke like you doing alone in a filthy place like this?"
    r "Well, Ma'am, he is hiding from 'em big ol gals tryina use him."
    e "Worry not, m'lord, this proud knight shall protect thee!"
    r "Oh dear, female knight, my personal guard! Ain't I a lucky man!"
    "We just stood there and laughed for the next few minutes."
    "I missed our foolish little talks. Louis is a great person, and a better friend."
    "But not nearly as imaginitive as Roland."
    e "God I missed you."
    show Roland happy at left
    r "I missed you too, love."
    e "Do you miss Louis?"
    show Roland upset at left
    r "Ehh..."
    show Lucy normal
    e "You don't have to tell me, if you don't want to"
    r "Sometimes... But it's complicated, love."
    e "You know I'm here for you."
    show Roland happy at left
    r "Yes!"
    e "But one day, you'll have to tell me what happened."
    show Roland upset at left
    r "Yes... And I will... Just, not today, I am not ready."
    e "It's ok."
    e "Oh, let's better start eating."
    show Lucy happy1
    show Roland happy at left
    r "Soooo... May I eat your momma's cooking again?"
    e "Sure thing, sweetie!"
    "As we started devouring our lunchboxes, I felt a pair of eyes on my back."
    "But I decided not to mind."
    $ show_Roland = True
    pause 0.5 
    $ Roland_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Roland = True
    
    $ renpy.pause()
    hide text with dissolve
    $ show_Roland = False
    hide Roland
    hide Lucy 
    with dissolve
    jump corridor
label classL:
    show bg classroom
    show Lucy happy1
    e "Louis!!! Momma wants to eat, momma loves yo momma's cooking!"
    show Louis flirty at right
    l "Oh, I will feed momma!"
    show Lucy pout
    e "Not like that!"
    e "Perv!"
    l "You know you love me the way I am!"
    show Lucy happy1
    e "Sure, now gimme da food!"
    l "Will do."
    l "Gotta feed the beast!"
    show Lucy shy
    e "Idiot."
    show Lucy normal
    e "Ne, why don't we invite Roland?"
    show Louis upset at right
    "I watched colour fade from his face as he looked at me with disbelief."
    l "Did- did he try to talk to you about me?"
    show Lucy shock1
    e "What- No, why?"
    l "Why are you mentioning it then?"
    show Louis angry at right
    e "I- I don't know why I shouldn't"
    l "I... I told you not to bother me about it."
    show Lucy angry 
    e "I lost a friend, and I don't know why, I think this matter needs to be resolved."
    show Louis awkward at left
    l "You're right."
    l "And you need to know what happened."
    l"Just not- not today, ok?"
    show Lucy normal
    e "Ok, whenever you're ready."
    show Louis normal
    l "Thank you."
    show Lucy happy1
    e "Now, gimme that food!"
    $ show_Louis = True
    pause 0.5 
    $ Louis_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Louis = True
    pause 0.5
    $ renpy.pause()
    hide text with dissolve
    $ show_Louis = False
    hide Louis
    hide Lucy
    with dissolve
    jump corridor
    
label corridor:
    show bg school_corridor_afternoon
    show Lucy tired
    "It's friday and school is almost over."
    if movie == 0:
        if observatorium == 0:
            if Jeremy_love == 20:
                "I don't know what I'll do, I'm not keen on the idea of wandering off at home and doing nothing."
                "I mean, I do like being alone and reading a few books, but this week has been so full of tests that I need to do something else to take my mind off of thing."
                show Jeremy smile at left
                j "Hey! Just the person I was looking for!"
                show Lucy happy1
                e "Hey, Jeremy!"
                j "Listen, It's friday night, and I have no plans for tonight."
                j "Wanna go and grab a cup of coffee or something?"
                e "Sure thing! I was just wondering what I'll be doing tonight!"
                j "Great!"
                $ show_Jeremy = True
                pause 0.5 
                $ Jeremy_love += 10
                show expression Text("{color=ffffff}+10 Love Points{/color}", 
                    size=50, 
                    yalign=0.5, # Centers the text -- Toward Bottom.
                    xalign=0.5, # Centers the text -- Toward Right. 
                    drop_shadow=(2, 2)) as text
                with dissolve
                $ show_Jeremy = True
                pause 0.5
                $ renpy.pause()
                hide text with dissolve
                $ show_Jeremy = False
                hide Jeremy
                with dissolve
                jump Jeremydate
            else:
                "I don't have anything to do"
                show Louis normal at right
                l "Hey, Mum told me to invite you for dinner. I Just got a new game, you up?"
                show Lucy happy1
                e "Yeah, sure thing!"
        else:
            "I can't find Louis anywhere, and he told me that he'll take me to the observatorium."
            "When, suddenly, I see him fighting with Roland"
            hide Lucy with dissolve
            show Louis angry
            show Roland upset at right
            with dissolve
            r "Can't you just let her make her own decisions?!"
            l "Just leave her alone, you can't just try to make things the way they were."
            l "You left us! You HURT US! Just because of your lack of ability to decide!"
            l "You can't just come back and pretend none of it happened."
            l "If she knew what you did- she'd never speak to you again."
            r "She'd understand."
            l "Don't be so selfish."
            e "Guys, what's going on?"
            show Roland sad at right
            show Louis upset 
            r "I- I have to go. See you later, Lucy."
            hide Roland 
            with moveoutright
            l "Hey, sweetie."
            show Lucy shock1 at right
            with dissolve
            e "What was that all about."
            l "Please, cane we talk about it later."
            e "I don't want to force you..."
            show Louis normal
            l "Thank you."
            show Lucy normal at right
            e "So... We're still going to the observatorium?"
            show Louis flirty
            l "We sure are!"
            l "Meet you at the station after school."
            show Lucy happy1 at right
            e "Sure!"
            $ show_Louis = True
            pause 0.5 
            $ Louis_love += 10
            show expression Text("{color=ffffff}+10 Love Points{/color}", 
                size=50, 
                yalign=0.5, # Centers the text -- Toward Bottom.
                xalign=0.5, # Centers the text -- Toward Right. 
                drop_shadow=(2, 2)) as text
            with dissolve
            $ show_Louis = True
            pause 0.5
            $ renpy.pause()
            hide text with dissolve
            $ show_Louis = False
            hide Lucy
            hide Louis
            with dissolve
            jump Louisdate
    else:
        "Suddenly I see Roland and Louis fighting."
        show Louis angry
        show Roland upset at right
        with dissolve
        r "Can't you just let her make her own decisions?!"
        l "Just leave her alone, you can't just try to make things the way they were."
        l "You left us! You HURT US! Just because of your lack of ability to decide!"
        l "You can't just come back and pretend none of it happened."
        l "If she knew what you did- she'd never speak to you again."
        r "She'd understand."
        l "Don't be so selfish."
        r "She's grown up, so have we."
        r "Won't You stop being so childish and let her make her own choices?"
        l "Well, you didn't give me much choice, did you?"
        l "After what you've done to ME."
        l "You do know you were MY fir-"
        e "Guys, what's going on?"
        show Louis upset
        show Roland sad at right
        show Lucy shock1 at left with dissolve
        l "Lucy!"
        l "What are you doing here?"
        e "Looking for Roland?"
        e "We were supposed to go to the movies together."
        l "Oh, really? Didn't I tell you to leave her alone?"
        e "Leave HIM alone, Louis, I won't tolerate this anymore."
        e "You either tell me what happened, or stop bothering us."
        "He glared at me, and, for a moment, I could see his dissapointment reflect in his eyes."
        hide Louis 
        with moveoutright
        e "Auch."
        e "I bet he's pissed."
        e "The movie's still on?"
        r "Are you sure you want to do this? I mean, Louis might think you're betraying him"
        e "Listen, he's not that stupid, he knows I'll do anything for him."
        e "But unless he tells me what's going on, and I conclude that you really ARE a bastard not worth mentioning, I'll continue doing my thing."
        e "I love him, I do, but I'm my own person and I make my own decision, and he knows it."
        r "Ok... If you're sure..."
        show Lucy happy1 at left
        e "Don't worry, Roland, it'll be allright."
        show Roland happy
        r "Thank you, meet you outside?"
        e "Sure thing."
        $ show_Roland = True
        pause 0.5 
        $ Roland_love += 10
        show expression Text("{color=ffffff}+10 Love Points{/color}", 
            size=50, 
            yalign=0.5, # Centers the text -- Toward Bottom.
            xalign=0.5, # Centers the text -- Toward Right. 
            drop_shadow=(2, 2)) as text
        with dissolve
        $ show_Roland = True
    
        $ renpy.pause()
        hide text with dissolve
        $ show_Roland = False
        hide Roland
        hide Lucy
        with dissolve
        jump Rolanddate
        
label Jeremydate:
    show bg cafe
    show Lucy happy1
    show Jeremy flirty at left
    e "Thank you for this."
    j "No, thank YOU."
    j "BTW, I don't mean to pry, but how come you didn't make plans with that guy that's always by your side?"
    show Lucy normal
    e "Louis? I honestly don't know what's going on, either."
    e "He's been acting odd ever since Roland started trying to, well, talk to me."
    j "Maybe he is jealous."
    e "Of whom, exactly?"
    show Jeremy normal at left
    j "You don't understand."
    j "Love is mixed up somewhere here."
    e "I don't believe it, there's no way Louis is in love with me."
    j "Well, he is in love with someone."
    j "Listen, I think you should stay out of it. The situation will calm down eventually, and you don't want to be a part of this."
    e "I guess you're right."
    show Jeremy flirty at left
    j "And there's no way they'll let go of a girl like you."
    show Lucy happy1 
    e "Oh, stop it you!"
    show Lucy shy
    e "And thank you, really, this means a lot."
    j "No problem, pretty lady."
    $ show_Jeremy = True
    pause 0.5 
    $ Jeremy_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Jeremy = True
    pause 0.5
    $ renpy.pause()
    hide text with dissolve
    $ show_Jeremy = False
    hide Jeremy
    hide Lucy
    with dissolve
    jump school2
    
label Rolandlove:
    show bg station
    show Roland flirty at left
    show Lucy happy1
    e "Thank you Roland, that was so fun!"
    r "No problem, I had a great time as well."
    e "I prefer the comic books, but this was surprisingly, well, good."
    r "I know what you mean, usually they mess everything up, and it's just mindless violence."
    e "I mean, more mindless violence than in the comics?"
    r "And kinda sexist."
    e "Yeah..."
    show Lucy normal
    e "On the serious note- you really don't want to tell me what's going on?"
    show Roland normal at left
    r "No.. Not now."
    show Ronald flirty at left
    r "This is our night, isn't it?"
    show Lucy shy
    e "Sure.."
    r "Wanna go and get some pancakes?"
    show Lucy happy1
    e "Pancakes! You do know I believe people generally don't enjoy food as much as they should."
    r "You sure do."
    show Lucy pout
    e "You meanie-"
    r "And you love me the way I am."
    $ show_Roland = True
    pause 0.5 
    $ Roland_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Roland = True
    $ renpy.pause()
    hide text with dissolve
    $ show_Roland = False
    hide Roland
    hide Lucy
    with dissolve
    jump school2
    
label Louisdate:
    show bg station
    show Louis flirty at left
    show Lucy happy1
    e "That was really cool!"
    l "I am aware of yout obsession with stars, yes."
    l "But that is to be expected, I have known you for years."
    e "True, true."
    e "I wonder if Roland still loves the stars."
    show Louis normal at left
    l "No."
    show Lucy pout
    show Louis upset at left
    e "No, really."
    l "No. I veto him."
    e "But- Louis-"
    l "I can't- honestlu, it's not up to me tell you, honestly."
    show Louis flirty at left
    l "And even if I were to tell you, it would't be on a beautiful night like this."
    e "Jerk."
    l "You love me the way I am, don't you."
    e "..."
    l "I'm buying you pancakes!"
    show Lucy happy1
    e "Yaaay!"
    l "You are so easy to manipulate!"
    e" No I'm not, but they better be dipped in chocolate!"
    $ show_Louis = True
    pause 0.5 
    $ Louis_love += 10
    show expression Text("{color=ffffff}+10 Love Points{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Louis = True
    pause 0.5
    $ renpy.pause()
    hide text with dissolve
    $ show_Louis = False
    hide Lucy
    hide Louis
    with dissolve
    
    jump school2

label school2:
    show bg classroom
    "School, school, school..."
    "I think nothing is as hellish as hours and hours of pure, distilled boredom."
    "As I listen to the professor recite the textbook- quite literally, I could feel his monotonous voice drilling a hole in my head."
    "I feel the voice of the seraphin promising me freedom- the bell rung. I felt my will to live return."
    show Lucy happy1
    e "Finally - lounch break, now I can finally do something that matters."
    show Louis flirty at left
    l "What, eat?"
    e "Exactly!"
    show Roland flirty at right
    r "Seriously, you never change."
    show Louis upset at left
    "Oh no, they're at it again."
    hide Louis
    hide Roland 
    with dissolve
    "I run away from them before they managed to drag me in."
    "And suddenly I see- "
    show Jeremy flirty at left
    with dissolve
    "Jeremy."
    j "Hey, sweetie, wanna grab some lunch?"
    menu:
        "Sure, I'm up for it.":
            jump rooftop2
        "I'm not really feeling up to it.":
            jump class3
    hide Lucy
    hide Jeremy
    with dissolve
    
label rooftop2:
    show bg rooftop
    show Lucy happy1
    show Jeremy flirty at left
    e "So, anything new?"
    
    
        
    
    
    
    
        
    
        
    