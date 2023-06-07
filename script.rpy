# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define av = Character("Ava")
define al = Character("Alice")
define k = Character("Katie")
define c = Character("Clarissa")
define s = Character("Sia")
define d = Character("Dylan")
define z = Character("Zack")
define p = Character("Peter")
define an = Character("Andrew")

# The game starts here.

label start:

    #Introduction of characters sequence

    #Need a description sequence.

    scene personal room c day
    with Dissolve(.5)

    "It is a new a day in early September."

    show ava happy at right

    av "What a beautiful morning! I can't wait to go to the university!"

    "This is Ava, the protagonist of the story. She's a freshmore at Academy University and is starting her first day today."

    pause .5

    #INSERT SKIP OPTION HERE
    "There's going to be a character introduction sequence where all the characters are introduced. Do you wish to go forward with the sequence or skip it?"

    menu:
        "Go forward with introduction sequence.":
             jump roll_intro_sequence

        "Skip the introduction sequence.":
            jump main_conflict

    label roll_intro_sequence:
        scene school a s1st2 day
        with Dissolve(.5)

        "Some time later..."

        show ava normal at right

        av "Oof I made it in time!"

        an "Ava! I am so happy to see you!"

        show andrew normal at left

        av "Hey Andrew! I am glad to see you too! How was your holidays?"

        an "My holidays were amazing! I went to Switz- ouch!"

        "Andrew gets shoved by a black haired girl."

        hide andrew normal

        show clarissa happy at left

        c "Ava!! I missed you so much!!"

        show ava happy at right

        av "Clarissa!! I missed you too!!"

        hide clarissa happy
        hide ava happy

        show andrew smug at right

        an "Wow girls, I can totally feel the love right now!"

        hide andrew smug

        show ava happy at right

        av "Haha! You know we also missed you, Andrew!"

        hide ava happy

        show clarissa smug at right

        c "I don't know Ava, I mean, who will miss a six feet cockroach?"

        show andrew smug at left

        an "I think Ava can handle it, given that a chimpanzee is currently by her side."

        "These two persons are Ava's friends. Their friendship goes back to middle school."

        "Ever since, Andrew and Clarissa have a small banter going on."

        hide clarissa smug
        hide andrew smug

        show ava happy at right

        av "I certainly missed you guys fighting!"
        av "Let's head for our new class, it's going to start soon."

        hide ava happy

        scene school a hallway st2 day
        with Dissolve(.5)

        s "Guys!"

        show sia normal at right

        s "Hey everyone!!"

        show ava happy at left

        av "Sia! It's great to see you again!"

        hide sia normal

        show sia happy at right

        "This is Sia, the last friend of their middle school friend group."

        s "I'm happy to see you guys too! Are you guys going to class?"

        av "Yeah, let's go together!"

        hide ava normal
        hide sia happy

        show clarissa smug at right
        show andrew smug at left

        c "I'm literally going to spray you with bug spray."

        an "Says the chimp who might not even know how it works!"

        hide clarissa smug
        hide andrew smug

        show sia normal at right

        s "These two are still going at it huh?"

        show ava normal at left

        av "You know it!"

        hide sia normal
        hide ava normal

        scene classroom a st2 day
        with Dissolve(.5)

        show male professor at right

        "Professor" "Welcome to this new term people! I hope you all enjoy this new experience!"
        "Professor" "Today's class will be more introductory so do not be too nervous."

        hide male professor

        pause (.5)

        "Some time later ..."

        show male professor at right

        "Professor" "That will be all for this class! I hope you guys enjoy this course!"
        "Professor" "Also, please do not forget to review what we went through in class!"

        hide male professor

        scene school a hallway st2 day
        with Dissolve(.5)

        show ava normal at right

        av "That was one very interesting class."

        show clarissa normal at left

        c "Yeah true, I am so hyped to start attending the laboratory sessions!"

        av "What do we hav- umph!"

        "Ava bumps into someone in the hallway."

        hide clarissa normal

        d "I'm so sorry, are you okay?"

        show dylan guilty at left

        "This is Dylan, who will eventually become Ava's crush."

        "Ava blushes at the sight of the unknown, handsome guy."

        hide ava normal

        show ava shy at right

        av "It's okay, no worries."

        hide dylan guilty

        show dylan normal at left

        d "I'll be on my way then."
        d "Katie, wait for me!"

        hide ava shy
        hide dylan normal
        hide katie normal

        show ava shy at right

        "Ava watches the guy leave and join a white-haired girl, her cheeks furiously blushing red."

        show katie normal at left

        "She is Katie, Dylan's childhood friend."

        hide katie normal

        show andrew normal at left

        an "Looks like someone just got struck by lightning."

        av "Oh stop it Andrew!"

        hide ava shy
        hide andrew normal

        pause (.5)

        scene school a gym s1st2 evening
        with Dissolve(.5)

        "Later that evening, Ava goes to meet the basketball club she just joined in the gym."

        "There are no training sessions on that day, just a casual meet-n-greet, where the students get to know their new teammates."

        show ava normal at right

        "She recognises some individuals from her morning class and approaches to befriend them."

        av "Hi, I'm Ava! I think we are all from the same class right? If it's okay with you all, can I join you guys?"

        show alice normal at left

        al "Hi Ava, sure. I'm Alice and these 2 doofuses are Peter and Zack!"

        hide alice normal

        show peter normal at left

        p "Please forgive Alice, Ava, she's a bit confused. The only doofus here is Zack."

        hide peter normal

        show zack normal at left

        z "Excuse me!"

        hide ava normal

        show ava happy at right

        av "It's a pleasure meeting you all! I look forward to playing with you guys!"

        hide zack normal

        "Alice, Peter and Zack are the first friends that Ava made at university. The three of them are previous highschool friends and they are thus close with each other."

        pause(.5)

        jump main_conflict

    label main_conflict:

        #start of main focus

        scene classroom a st2 day
        with Dissolve(.5)

        "A few weeks go by before it is finally the time where Ava has to choose her group for the project."

        "In the meantime, she got closer to her new friends and also managed to befriend her crush Dylan."

        show male professor at right

        "Professor" "Do not forget to submit your group by next week Monday."
        "Professor" "Have a good rest during the weekend and see you guys next week!"

        hide male professor

        show ava normal at right

        "Ava is currently thinking to herself..."

        av "I suppose I should be joining Clarissa, Andrew and Sia for the project."

        show dylan normal at left

        "Dylan suddenly walks towards to Ava."

        d "Hey Ava!"

        hide ava normal

        show ava shy at right

        av "Hey Dylan! What's up?"

        d "About the group project, I currently have 3 people in my group and we are missing one person. Do you want to join us?"

        av "Oh! Thanks for thinking of including me! I need to think about it first, is okay if I let you know later?"

        d "Sure, I hope we get to work together."

        av "Catch you later!"

        hide ava shy

        hide dylan normal

        pause(.5)

        scene school a stairs st2 day
        with Dissolve(.5)

        "Later that day.."

        show ava normal at right

        "Ava is walking down the stairs to go to the library. On her way there, she bumps into Alice."

        show alice normal at left

        al "Ava!! Hey!! How are you? You know, I was just looking for you!"

        av "Hi Alice! I'm good. I'm just heading to the library for some self-study. Why were you looking for me?"

        al "So, you remember the group project that Prof mentionned today. Zack, Peter and I were thinking to ask you to join our group. It will be so cool if we work together!"

        av "Ohh, thanks for asking me Alice, I'm glad. Is it okay if I get back to you on that later? I still need to think about that for a bit."

        al "Sure thing, Ava! See you later!"

        hide ava normal
        hide alice normal

        pause(.5)

        scene school a s4st2 day
        with Dissolve(.5)

        "Some time later..."

        show ava normal

        av "What should I do now? Should I stick my old friends? Join Dylan? Or join Alice and the gang? I'm so confused!"

        #the route choice

        menu:
            "Join her old friends.":
                jump old_friends_route

            "Join Dylan's group.":
                jump crush_route

            "Join her new friends.":
                jump new_friends_route

        label old_friends_route:

            #Start of old friends' route

            av "Since I am more comfortable with my friends and we know each other's strengths and weaknesses, I'd rather join them."

            show text "You have currently made a decision based on an unconscious bias known as Familiarity Bias! This bias stems from the innate human tendency to seek familiarity and safety in our social interactions." at top
            with dissolve
            pause (9)
            hide text
            with dissolve

            "She then proceeds to send a text message to both Dylan and Alice informing them about her decision."

            pause(.5)

            scene school a hallway st2 day
            with Dissolve(.5)

            show ava normal at right

            av "Hey guys! You want to meet up later after school to discuss the school project?"

            hide ava normal

            show sia normal at right
            show clarissa normal at left
            show andrew normal


            "All" "Sure thing!"

            hide sia normal
            hide andrew normal
            hide clarissa normal

            pause(.5)

            "Later that day..."

            scene clubroom a st2 day
            with Dissolve(.5)

            show andrew normal at right

            an "We can use this space to discuss! I reserved it from some of my seniors from the Art Club."
            an "As long as we do not touch or take anything here, we should be fine!"

            show sia normal at left

            s "Great! Shall we start?"

            hide sia normal
            hide andrew normal

            pause(.5)

            scene clubroom a st2 evening
            with Dissolve(.5)

            "Some hours later..."

            show clarissa tired at right

            c "I'm so tired guys! Can we call it a day? I think we made significant progress today."

            show ava normal at left

            av "Sure! We can continue another day. We managed to settle on our main point, so that's good!"

            hide ava normal
            hide clarissa tired

            show andrew normal at right

            an "Then we end the project meeting here! That's good timing because Sia's volleyball practice starts soon."
            an "Let's all leave!"

            hide andrew normal

            "Ava's phone suddenly rings."

            show ava normal at right

            av "Sorry guys, I need to pick up this call! You all can leave first, I will leave after the call. Don't worry Andrew, I'll make sure to lock the door of the club when leaving!"

            show andrew normal at left

            an "Okay Ava! You can drop the key at the Art & Crafts keys' lockroom. See you tomorrow!"

            hide andrew normal

            "Ava proceeds to pick up the phone and talk with the calller."

            hide ava normal

            pause(.5)

            scene school a s1st2 night
            with Dissolve(.5)

            "After the call, Ava does as Andrew instructed her and returns home."
            "As she relaxes at home that night, she is very unaware of how things will be turning out the next day!"

            pause(.5)

            #start of conflict

            scene school a s1st2 day
            with Dissolve(.5)

            "The next day, at school..."

            show andrew angry at right

            an "Guys, I have really bad news!"

            show ava serious at left

            av "What happened, Andrew?"

            an "One of my seniors' uncompleted canva went missing!"
            an "They discovered it this morning went they went to open the Art room."
            an "Additionally, the room was a complete mess. There was paint splattered everywhere and the brushes were all over the floor!"

            hide ava serious

            show ava shocked at left

            av "What? That's terrible!"

            hide ava shocked

            show ava serious at left

            an "Ava, are you sure you locked the door before leaving?"

            av "Yes Andrew, I'm confident I locked the club's door before leaving."

            an "Well, someone magically came in and wrecked havoc in the club then!!"

            hide ava serious

            show ava shocked at left

            av "You... you are not blaming me, are you Andrew?"
            av "Do you really think I have done that?"

            an "What else should I think Ava?"
            an "You are the last one who left the room, you stayed there alone for an unspecified amount of time and according to you, there is no one else who came to the room after we left!"
            an "Who else can it be?"

            av "This is not happening right now! How could you blame me Andrew? You know I am not the kind of person to do something so mean!"

            an "I don't know Ava, but right now, you are not exactly looking too innocent!"

            hide ava shocked

            show ava sad at left

            hide andrew angry

            show clarissa serious at right

            c "Cut it down Andrew! You're blaming Ava based on very circumstantial proof right now. Do not forget that she is our friend and she will never do something like that!"

            hide ava sad

            show sia serious at left

            s "Well, who else could have done it? Like Andrew said, no one else could have come in after we left and Ava is the last person to come in!"
            s "Everything points towards her, she obviously has a hand in it, even if she's not the culprit!"

            hide clarissa serious

            show ava sad at right

            av "Guys please stop fighting! Let's all resolve this together!"

            hide sia serious

            show andrew angry at left

            an "I am done with you here! I'll be expecting your apologies and you compensating the seniors for the damage caused before this becomes too serious. I can't believe you're someone so evil."
            an "Before you do so, just refrain from talking to me!"

            hide andrew angry

            "Andrew then leaves the room, Sia following him."

            show text "You just experienced Andrew using his confirmation seeking bias where he interpreted the situation in a way that fits his hypothesis while disregarding conflicting evidence." at top
            with dissolve
            pause (9)
            hide text
            with dissolve

            show clarissa serious at left

            c "Don't worry Ava, I know you did not do anything wrong! Andrew is just ... stressed right now. I know he will come around his senses and apologise for his behaviour later."

            av "I am so overwhelmed, Rissa. I know he's just stressed but I'm so hurt by what he and Sia said."

            c "It's okay Ava, I'm sure we will make up in no time and we will all try to solve this issue together."

            pause(.5)

            hide clarissa serious
            hide ava sad

            scene school a s1st2 evening
            with Dissolve(.5)

            "However, contrary to Clarissa's belief, neither Andrew nor Sia even talked to Clarissa that day."

            show clarissa angry at right

            c "I'm so angry that those two are still blaming you."

            show ava sad at left

            av "It's okay, I understand, I would probably have been same have I been in their place."

            hide clarissa angry

            show clarissa serious at right

            c "I highly doubt it Ava. I don't think you're someone who will blatantly accuse their friend once things go wrong."

            av "Thanks for trusting me, Rissa, it means a lot."

            c "I know you're innocent Ava, you're such a nice person, so I know you are not the culprit. I can't understand why those two blockheads are not understanding that."
            c "There is one way to make them understand though, we need to find concrete evidence to show them that you are not the culprit."

            av "You're right, we should do that. Can you help me to do so Clarissa?"

            c "Of course, don't worry, I'll get you out of this mess, Ava!"

            hide clarissa serious
            hide ava sad

            scene school a hallway st2 day
            with Dissolve(.5)

            "The next day, Ava and Clarissa spend their free time talking to random students to try to find out after Ava left the Art club room. To their disappointment, no one saw anything as it was quite late and there were few students that stayed in the university at that time."

            show clarissa serious at right

            c "I cannot believe that no one saw anything. I thought at least someone saw something. This is becoming more and more complicated!"

            show ava serious at left

            av "Same! At this point, there's no way we can find the true culprit and find my innocence."

            c "Oh, I realised there's one sure way left!"

            av "Which is?"

            c "Examining the security footage of that day! If I recall correctly there is a CCTV camera focusing on the entrance of the Art room. It should have definitely captured all the people entering and leaving the art room!"

            hide ava serious

            show ava normal at left

            av "Clarissa, you're a genius! You are right! The security footage would have definitely captured the culprit! Let's head to the security guard room and request their help to view the footage!"

            hide ava normal
            hide clarissa serious

            "Ava and Clarissa go to the security office and explain their circumstance to them. Luckily, the security guards understand the urgency if the situation and help them to view the footage of that day."
            "The footage shows that someone indeed broke in the Art club and left some time later with a canva held under their arm. The girls managed to find the culprit."
            "They request the security guards to send this particular recording of the footage to them and after that thanked them for their help."
            "They then decide to confront Andrew and Sia with the evidence they have."

            pause(.5)

            scene school a hallway st2 evening
            with Dissolve(.5)

            "Andrew comes first, Sia being late owing to her volleyball practice ending a bit late."

            show andrew serious at right

            an "So, you have finally decided to confess, Ava?"

            show ava serious at left

            av "Hold your horses Andrew. Clarissa and I have evidence that someone else entered the room after me and wrecked the Art room."

            an "Well, show me then, I am so interested in that 'evidence' you have."

            "Ava then proceeds to show the video recording to Andrew from her phone."

            hide ava serious
            hide andrew serious

            show andrew serious

            hide andrew serious

            show andrew shocked

            pause(.8)

            hide andrew shocked

            show andrew guilty

            "Andrew's face shows a change of emotions from expresionless to shock to guilt."
            "He sees clearly on the footage who the culprit is. He cannot believe his eyes."

            hide andrew guilty

            "At the same time, Sia comes in."

            show sia serious

            "Are you finally confessing then Ava?"

            hide sia serious

            show sia serious at right
            show andrew serious at left

            an "It's you!"

            s "I am sorry?"

            hide sia serious

            show sia shocked at right

            an "The culprit, it's YOU!"

            "Sia becomes frozen in shock. Andrew then turns the phone screen towards her and shows her the video playing."
            "Sia is seen entering the Art room in her volleyball outfit and after 30 minuttes or so, she leaves the room with the canva under her arms."

            hide sia shocked

            show sia sad at right

            s "I... I can explain..."

            an "How could you Sia? You wrecked the Art room and stole my seniors' artwork? And worst of it, you later had the guts to hide and lie about it while you joined me in blaming Ava?"

            s "I'm so so sorry Andrew, my intentions are completely different from what it may seem!"

            hide andrew serious

            show clarissa serious at left

            c "No matter what the reason may be, you still have wronged us Sia!"
            c "It's time for you to face the consequences, what do you say Andrew?"

            hide clarissa serious
            hide sia sad

            show andrew serious

            menu:
                "Yeah, Sia, it is time for you to face bear the brunt of your action.":
                    jump sia_bears_blame

                "Let's not be too mean to Sia, she did say she had a reason to do so.":
                    jump sia_let_off

                "I am not sure, I don't know what to do!":
                    jump andrew_no_choice

            label sia_bears_blame:

                show text "The option you chose has allowed Andrew to overcome his confirmation seeking bias and he has taken a fair decision." at top
                with dissolve
                pause (9)
                hide text
                with dissolve

                hide andrew serious
                show andrew serious at right

                an "It is high time to pay up for the repercussions of your actions, Sia."

                show sia sad at left

                s "Okay Andrew."

                hide andrew serious
                hide sia sad

                show sia sad
                "She then proceeds to fetch the stolen canva that she secretly stashed in her gym locker."
                "She also hands over the money that the club needs for repairs and replacement of materials to Andrew."

                hide sia sad

                show ava serious at right

                av "Why did you do that, Sia?"

                show sia sad at left

                #Start of bonus story

                jump choice_done

            label sia_let_off:

                show text "The option you chose did not allow Andrew to overcome his confirmation seeking bias as he is reluctant to shift the blame to Sia despite all evidences pointing towards her." at top
                with dissolve
                pause (9)
                hide text
                with dissolve

                hide andrew serious
                show ava angry at right

                av "Excuse me!! Andrew!! What do you mean she had a reason to?"
                av "What about me? Why are you treating her better than the way you are treating me?"
                av "Did you want me to be the culprit that bad?"

                show andrew guilty at left

                an "No Ava, that's not my intention!"

                hide andrew guilty
                hide ava angry

                show ava angry

                av "Enough is enough!"

                menu:
                    "Sia, tell me why you did that?!":
                        jump confront_friend

                    "I just want to leave this mess!":
                        jump let_friend_go

                label confront_friend:

                    show text "The option you have chosen has allowed Ava to break out of her familiarity bias. She is currently talking to Sia in a tone of unfamiliarity." at top
                    with dissolve
                    pause (9)
                    hide text
                    with dissolve

                    hide ava angry

                    show ava angry at right

                    av "So Sia, do you care to explain yourself?"

                    show sia sad at left

                    s "I'm so sorry Ava. If I could go back in time, I would have never done such a thing!"

                    jump choice_done

                label let_friend_go:

                    show text "The option you have chosen has not allowed Ava to break out of her familiarity bias. She is so shocked that she would rather let Sia go than to confront her." at top
                    with dissolve
                    pause (9)
                    hide text
                    with dissolve

                    jump choice_done

            label andrew_no_choice:

                show text "The option you chose did not allow Andrew to overcome his confirmation seeking bias as he is reluctant to shift the blame to Sia despite all evidences pointing towards her." at top
                with dissolve
                pause (9)
                hide text
                with dissolve

                jump choice_done

        label crush_route:

            "it's"

            jump choice_done

        label new_friends_route:

            "me.."

            jump choice_done

        label choice_done:
            # This ends the game.
            return
