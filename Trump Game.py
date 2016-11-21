print ("The year is 2036, and Donald Trump has been president for over 20 years. "
       "America has become a post-apocalyptic wasteland following the events of World Wars III, IV, and VI "
       "(Americans have forgotten how to count). Outraged by these events, you have decided to try and kill Donald Trump once and for all.")

race=str(input("Would you like to be white, black or asian?(All other races have been eliminated by the Donald)"))
choice=("You have chosen to be ", race)
money=0
global money
global inventory
global choice
inventory=[]
Trump=("alive")
while money >= 0 and Trump==("alive"):
    global money
    global inventory
    if race=="white":
        money=money+200
        print("You have", str(money), "dollars")
        choice=str(input("The first thing you need is a weapon, would you like to go to the gun shop or the knife shop?"))
    elif race=="black":
        money=money+50
        print("You have", str(money), "dollars")
        choice=str(input("The first thing you need is a weapon, would you like to go to the gun shop or the knife shop?"))
    elif race=="asian":
        money=money+100
        print("You have", str(money), "dollars")
        choice=str(input("The first thing you need is a weapon, would you like to go to the gun shop or the knife shop?"))

    def gun():
        global money
        global inventory

        if race=="black" or race=="asian":
            print("You attempt to buy a gun, but the white store owner shoots you in the shoulder. "
                  "On the loudspeakers, you hear the recent announcement by his holiness (as you must call him) Trump, "
                  "all hospitals have been shut down due to the middle class not paying enough taxes.")
            wound=str(input("Do you want to attempt surgery on yourself, or would you rather deal with the wound?"))
            if wound == "surgery":
                    surgery()
            elif wound == "deal with it":
                    deal()
        elif race=="white":
            print ("You get to buy a gun, albeit at a high cost. You don’t have much money left, "
                   "as you waste 90 dollars on this weapon.")
            money = money-90
            inventory.insert(0,"gun")
            travel=str(input("Realising you need to journey to washington DC, would you like to try and hitch a ride or take a train?"))
            if travel == "hitch a ride":
                hitchride()
            elif travel == "train":
                train()
    def knife():
        if race=="white":
            print ("You get questioned why you would need a knife by the asian owner, "
                   "but you still get the knife, though at a high price of 80 dollars")
            money = money - 80
        elif race=="black":
            print ("You get asked why you need a knife, but the knife owner is your old friend "
                   "and you are able to buy the knife at a really cheap price of 20.")
            money = money - 20
        elif race=="asian":
            print ("The asian owner sees you and passes you a knife for free. you catch a break, "
                   "as he also hands you a train ticket to washington DC." )
            train()

    def bodyguard():
        global Trump
        if race=="white":
            print("If you are white, you are able to buy a tuxedo and was able to obtain"
                  "access to the White House using a stolen ID.")
            if "knife" in inventory:
                print("You close in on Trump and stab him, but his personal bodyguards are able to shoot you away and then save him. You have failed.")

            else:
                print("You corner Trump in a hallway before shooting him and fleeing. Trump is dead.")
                Trump="dead"

        elif race=="asian":
            print("If you are black, the moment Trump see’s you in the White House"
                "you were arrested and killed in his torture chambers. Too bad.")

        elif race=="black":
            if "knife" in inventory:
                print("you were able to gain access to the white house and you are attempting"
                      "to get close to Trump and stab him in the heart. You sneak away and live the rest of your life in peace.")

            else:
                print("You were able to gain access to the white house,"
                      "but without a knife you have no way of finishing off the job. Trump's chief of security smells something fishy"
                      "about you and has you sent to a secret facility in Alaska. Needles to say you are never heard of again.")

    def surgery():
        print ("attempt surgery")
    def deal():
        print ("deal with wound")

    def hitchride():
        if race=="white":
            print ("You flash the hitchhiker sign, but it is a black family that drives in the car past you."
            "They get out and mug you, stripping you of 80 dollars and the weapon you obtained. Luckily,"
            "a white family passes by you on the road and takes you to DC. they give you some medicine that you may need later.")
            inventory.insert(0,"medicine")
            if "gun" in inventory:
                choice=str(input("Would you like to infiltrate Trump's house as a potential bodyguard or use your gun as a sniper to shoot him dead?"))
                if choice=="sniper":
                    sniper()
                elif choice=="bodyguard":
                    bodyguard()
            else:
                print ("Because you do not have a gun, you have to infilitrate Trump's house as a bodyguard.")
                bodyguard()
        if race=="black":
            print("A car with a black family heading to DC sees you and picks you up."
            "They drive you into DC and pass you a gun on your way out. ")
            if "gun" in inventory:
                trump=str(input("Would you like to infiltrate Trump's house as a potential bodyguard or use your gun to shoot him dead?"))
                if trump=="sniper":
                    sniper();
                else:
                    bodyguard();
            else:
                print ("Because you do not have a gun, you have to infilitrate Trump's house as a bodyguard.")
                bodyguard()
        if race=="asian":
            print("A black family passing by just ignores you. And you are unable to get anything. After 3 hours of waiting",
            "you offer to pay 50 dollars to anyone who will take you and get yourself a ride. 50 dollars short, you finally reach the capital."
            "now that you're here, you need to decide how you will kill Trump.")
            money=money-50

            if "gun" in inventory:
                choice=str(input("Would you like to infiltrate Trump's house as a potential bodyguard or use your gun to shoot him dead?"))
                if choice=="sniper":
                    sniper()
                elif choice=="bodyguard":
                    bodyguard()
            else:
                print ("Because you do not have a gun, you have to infilitrate Trump's house as a bodyguard."),
                bodyguard()

    def sniper():
            print("You were able to find a hidden spot near the White House.",
            "When Doanld Trump came out and made a speech, you decided to kill him on the spot to end it once and for all",
            "You were able to hit him after 2 misses and he dropped dead immediately."
            "Although you were arrested for murder immediately, you will be recognized as a international hero for centuries to come.")


    def train():
        print ("train")


    if choice=="knife":
        knife()
    elif choice=="gun":
        gun()

    else:
        print ("You have failed in your mission.")



