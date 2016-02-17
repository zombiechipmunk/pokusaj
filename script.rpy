# You can place the script of your game in this file.

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
                xalign = 0.5,
                ypos = 400,)
            ui.vbox(xalign = 0.5)
            ui.text ("Roland's Love points: %d" %Louis_love,
                xalign = 0.5)
            ui.bar(max_love, Roland_love,
                style = "my_bar")
            ui.close()
            
            if show_Jeremy:
            ui.frame(
                xalign = 0.5,
                ypos = 400,)
            ui.vbox(xalign = 0.5)
            ui.text ("Jeremy's Love points: %d" %Louis_love,
                xalign = 0.5)
            ui.bar(max_love, Jeremy_love,
                style = "my_bar")
            
            ui.close()
        
    config.overlay_functions.append(stats_overlay)
init -2 python:
    Louis_love = 10
    max_love = 150
    
    Jeremy_love = 10
    max_love = 150
    
    Roland_love = 10
    max_love = 150
    
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
    


define e = Character('Lucy', color="#FFC0CB")
define r = Character('Roland', color= "#8B2500")
define l = Character("Louis", color = "#0000CD")
define j = Character("Jeremy", color = "#00BFFF")
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
image Lucy happy1 = im.Scale("smile3.png",250,600)
image Lucy happy2 = im.Scale("smile1.png",250,600)
image Roland normal = im.Scale("MS2-smile1.png", 250, 700)
image Roland flirty = im.Scale("MS2-wink2.png", 250, 700)
image Roland happy = im.Scale("MS2-smile6.png",250,700)
image Roland upset = im.Scale("MS2-upset1.png",250,700)
image Roland sad = im.Scale("MS2-sad.png",250,700)
image Louis flirty = im.Scale("MS1-wink.png",400,700)
image Louis normal = im.Scale("MS1-default.png",300,700)
image Louis upset = im.Scale("MS1-awkward.png",400,700)
image Louis unhappy = im.Scale("MS1-pout.png",400,700)
image Jeremy surprised = im.Scale("MS3-surprised2.png",300,700)
image Jeremy smile = im.Scale("MS3-smile5.png", 300, 700)
image Jeremy normal = im.Scale("MS3-default.png",300,700)
image Jeremy flirty = im.Scale("MS3-wink.png",300,700)
image Jeremy shy1 = im.Scale("MS3-shy1.png",300,700)
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
    show expression Text("{color=ffffff}{font=LHFmisterkookyREG_0.TTF}+50 Love Points{/font}{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Roland = True
    
    $ renpy.pause()
    $ hide text with dissolve
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
    show expression Text("{color=ffffff}{font=LHFmisterkookyREG_0.TTF}+50 Love Points{/font}{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Louis = True
    pause 0.5
    $ renpy.pause()
    $ hide text with dissolve
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
    show Jeremy surprised at right
    e "Eh, sorry, I have to go, I have to... I know that..."
    e "EEEEH!"
    hide Lucy shock1
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
    show Jeremy laughing at right
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
            jump Roland 1
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
    show expression Text("{color=ffffff}{font=LHFmisterkookyREG_0.TTF}+50 Love Points{/font}{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Louis = True
    pause 0.5
    $ renpy.pause()
    $ hide text with dissolve
    $ show_Jeremy = False
    jump continue2
    hide Jeremy flirty
    return
    
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
    show expression Text("{color=ffffff}{font=LHFmisterkookyREG_0.TTF}+50 Love Points{/font}{/color}", 
        size=50, 
        yalign=0.5, # Centers the text -- Toward Bottom.
        xalign=0.5, # Centers the text -- Toward Right. 
        drop_shadow=(2, 2)) as text
    with dissolve
    $ show_Louis = True
    pause 0.5
    $ renpy.pause()
    $ hide text with dissolve
    $ show_Louis = False
    
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
    jump continue2
    return
    
    
        
    

    
    