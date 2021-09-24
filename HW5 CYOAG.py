def main():
    doneplaying = False

    while doneplaying == False:
    
        PlayGame()
        print("Do you want to play again? Type yes or no.")

        user_answer = input()
        
        if user_answer == 'no':
            doneplaying = True
            
    print("Thanks for playing. Goodbye.")
    
    
def PlayGame():
    print("*BEEP BEEP BEEP* It's 4:30 a.m. You wake up, get dressed and head")
    print("downstairs for coffee. You've got a call shift at the hospital in")
    print("one hour. ")
    print("You sit down on the couch and flip on the news.")
    print()
    print("WARNING, WARNING!! EMERGENCY P.S.A.!!, 'blares your T.V.'")
    print("--New York is already overwhelmed. THIS IS NOT A JOKE. People")
    print("are fleeing the city as droves of them swarm in. This is what we")
    print("know so far.")
    print("    Zombies will eat you, they do not have thoughts or feelings.")
    print("    Kill them on sight. There is no cure for this disease. The")
    print("    CDC has a vaccine that will PREVENT YOU FROM TURNING WHEN")
    print("    YOU DIE. All survivors will report to Atlanta, GA immediately")
    print("    for vaccination. Many of you will die on the trip. We recommend")
    print("    carrying weapons, they will die if you damage the brain or the")
    print("    heart. Sleep in trees, on roofs, or in boats. They cannot swim")
    print("    or climb, and will go away if they cannot reach you. Bring")
    print("    food and fuel. You will need it. Take solice in the fact")
    print("    that if you reach us, you will be safe. We have gates, food,")
    print("    medicine, and shelter. Good luck.")
    print()
    print("You immediately get up and pack everything you need. You take")
    print("food, water, fishing gear, a first aid kit, and a knife. Then")
    print("you?")
    print("    1) drive to the CDC headquarters in Atlanta, GA.")
    print("    2) call your pilot friend and plan to meet at the airport.")
    
    user_choice = GetUserInput()
    version = 1
    
    if user_choice == 1:
        GoCDC(version)
    elif user_choice == 2:
        goAirport()


def GetUserInput():
    print("Enter 1 or 2")
    user_input = int(input())
    return user_input


def GoCDC(version):
    if version ==1:
        print("You get in your car and drive to the gas station for fuel.")
        print("On the way, you see a woman. She waves and screams for help.")
        print("You?")
        print("    1) pull over to help. You offer her some food and a ride.")
        print("    2) keep driving. You can't afford to run out of supplies.")
    elif version == 2:
        print("You fly to the Atlanta. You land at the closest airport to the CDC")
        print("and steal a courtesy car but it's low on gas. You'll need to stop")
        print("at the nearest station. On the way, you see a woman who needs")
        print("help. You?")
        print("    1) pull over to help. You offer her some food and a ride.")
        print("    2) keep driving. You can't afford to run out of supplies.")
        version = 3
        

    user_choice = GetUserInput()

    if user_choice == 1:
        helpwoman(version)

    elif user_choice == 2:
        donthelp()

def donthelp():
    print("You are unable to get fuel, and you get stranded at the gas station.")
    print("You?")
    print("    1) wait for help.")
    print("    2) start walking to the CDC.")

    
    user_choice = GetUserInput()

    if user_choice == 1:
        print("You wait on the roof for almost two days, hoping someone will")
        print("save you. Unfortunately, you run out of rations and starve to death.")

    elif user_choice == 2:
        startwalking()

def startwalking():
    print("On your way, you encounter a zombie. You run. It chases you for nearly a")
    print("mile, and you realize you can't run anymore. You?")
    print("    1) fight it")
    print("    2) hide")

    user_choice = GetUserInput()

    if user_choice == 1:
        print("You're too tired. You lose the fight with the zombie, and it rips")
        print("your face off. That's kinda a rough way to die.. and you were so close..")
        print("too bad..")

    elif user_choice == 2:
        print("You make it to the CDC, surprised to see that the woman you passed earlier")
        print("also made it. You become close friends, no hard feelings. But in time, you")
        print("forget your betrayal. She does not... Thirty years later, she slits your")
        print("throat in your sleep, and is never caught.")
        

def goAirport():
    print("Your friend meets you at the airport hangar where he stores his plane.")
    print("As he is opening the door, several zombies notice the noise and rush over.")
    print("You?")
    print("    1) climb the side of the building and wait it out.")
    print("    2) fight them with your knife.")

    user_choice = GetUserInput()

    if user_choice == 1:
        waitItOut()
    elif user_choice == 2:
        fightZombies()
        
def waitItOut():
    print("You both make it to the roof and after a few hours the zombies wander off.")
    print("You take these hours to discuss your plans for surviving the apocalypse.")
    print("You think flying to the CDC is a good option, but your friend thinks that")
    print("his private island is a better idea. You?")
    print("    1) choose to fly to the cdc.")
    print("    2) choose to fly to the island.")
    
    user_choice = GetUserInput()
    version = 2

    if user_choice == 1:
        GoCDC(version)
    elif user_choice == 2:
        goIsland()

def goIsland():
    print("You and your friend fly to his island. You have a shelter, clean water,")
    print("and plenty to eat. You spend your mornings fishing on the beach,")
    print("and your afternoons relaxing. Life is good and you survived the")
    print("zombie apocalypse. Congratulations.")

def fightZombies():
    print("You fight the zombies together and get away, but your friend is bit")
    print("on the hand. As a doctor, you know hes at risk of turning or getting")
    print("an infection. He's also your only way to the island. You?")
    print("    1) amputate the hand, using your first aid kit and knife.")
    print("    2) bandage the hand and hope for the best.")

    user_choice = GetUserInput()

    if user_choice == 1:
        amputate()
    elif user_choice == 2:
        bandage()

def amputate():
    print("Cutting off your friend's hand isn't fun, but he lives.")
    print("He is able to tell you how to fly out of there and on the way")
    print("you see two islands--your friend's island and another bigger island.")
    print("You?")
    print("    1) head for your friend's island.")
    print("    2) head for the other island.")

    user_choice = GetUserInput()

    if user_choice == 1:
        friendisland()
    elif user_choice == 2:
        otherisland()

def bandage():
    print("Your friend turns into a zombie an hour later. You kill him")
    print("but can't fly anywhere. You survive for a few months, living in")
    print("the airport hanger, but the zombies do eventually overwhelm and eat you.")

def friendisland():
    print("You make it to his island. You have a shelter, clean water,")
    print("and plenty to eat. You spend your mornings fishing on the beach,")
    print("and your afternoons relaxing with your friend. Unfortunately, he dies a")
    print("month later due to infection complications, and because neither of you")
    print("are vaccinated, he turns and eats your brains.")

def otherisland():
    print("You misjudged the distance, and you run out of fuel before you make it.")
    print("The plane is swallowed by the sea and you're never heard from again.")
    
def helpwoman(version):
    print("She thanks you and reveals that she has a bow and one arrow left.")
    print("You can't get gas, but she hotwires a car. You travel together.")
    print("You tell her you don't have enough food, and you must")
    print("find more soon if you want to survive. You?")
    print("    1) Try your luck fishing")
    print("    2) Go hunting")

    user_choice = GetUserInput()

    if user_choice == 1:
        gofishing(version)
    elif user_choice == 2:
        gohunting(version)

def gohunting(version):
    print("The woman manages to take down a deer with her bow, ")
    print("however, her arrow is damaged and unusuable.")
    print("After cooking the meat and camping for the night, you decide")
    print("to continue driving in the morning. ")
    print("About an hour's walk from CDC headquarters your car runs out of gas.")
    print("You encounter a zombie. You?")
    print("    1) fight it with your knife.")
    print("    2) trip the woman and run.")

    user_choice = GetUserInput()
    if version !=3:
        version = 2

    if user_choice == 1:
        fightzombie()
        
    elif user_choice == 2:
        tripher(version)
    

def gofishing(version):
    print("You go fishing. You?")
    print("    1) Use some of your leftover food as bait.")
    print("    2) Use a fishing lure.")

    user_choice = GetUserInput()

    if user_choice == 1:
        leftoverfood(version)
        
    elif user_choice == 2:
        lure()

def lure():
    print("You fish for hours, with no luck. Your companion gives up on you")
    print("after a days worth of wasted energy and continues on her own.")
    print("You starve to death.")

def leftoverfood(version):
    print("You catch as many fish as you can eat, and get")
    print("back on the road quickly. The car runs out of gas,")
    print("but you're almost to the CDC. You encounter a zombie")
    print("on your way. You?")
    print("    1) fight it with your knife.")
    print("    2) trip your companion and run.")

    user_choice = GetUserInput()
    if version !=3:
        version = 1

    if user_choice == 1:
        fightzombie()
        
    elif user_choice == 2:
        tripher(version)

def fightzombie():
    print("You win the fight, and you make it to safety at the")
    print("CDC. You fell in love with the woman on the way, and now that all survivors")
    print("are vaccinated, you both have jobs killing zombies. The world")
    print("is getting closer to normal every day, life is good, and you")
    print("live long happy lives together.")

def tripher(version):
    if version == 1:
        print("As you run, you hear the unmistakable twang of a bowstring being released.")
        print("You feel the arrow stick deep in the back of your thigh, severing your hamstring.")
        print(" \"You tried to kill me!\" She calls out as she runs by you, leaving you to the zombie.")
        print("You watch her make it to the CDC from Hell.")
    elif version ==2:
        print("As you run, you hear the sounds of her screaming in agony as her")
        print("flesh is eaten by the zombies. \"Why? Why me?\" are her final words")
        print("as she is ripped apart.")
        print("You make it to the CDC, but you'll have to live with the guilt of ")
        print("what you did for the rest of your life.")
    elif version ==3:
        print("The zombies rip her apart. You and the pilot escape and make it")
        print("to the CDC, but he rats you out for sacrificing her. The US military")
        print("sentences you to be exiled, and you are sent back out into the city")
        print("where you build a safe-ish place to live, but you lose your mind, and")
        print("kill anything that gets in--even humans.")


main()
