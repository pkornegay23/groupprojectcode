##intro
def intro():
    """The user is introduced to the game.

    The user is told the background story of the jewel. Then the user is given
    three possible suspects of who stole the jewel. The user is prompted to choose
    to chase after the mage, ambassador, or a relative.
    Depending on which option the user chooses a different function is called.
    """
    print("")
    print("The jewel was last seen worn by the princess at the annual ball")
    print("The last three people the princess interacted with were the mage, a group of ambassadors, and her relative.")
    answerside = input("Who do you want to go after for the jewel: type 'mage', 'ambassador', or the 'relative'? ")
    if (answerside == "mage") :
        gomage()
    elif (answerside == "ambassador") :
        goambassador()
    elif (answerside == "relative") :
        gorelative()
    else:
        print("Invalid answer. Why don't you try again?")
        intro()

##Eleanor's Code
def goambassador():
    """This is the first function for the ambassador option.

    The function directs the user to find the ambassadors. The user is 
    prompted to speak with an innkeeper or look for carriages.
    Depending on the users choice a different function is called.
    """
    print(" ")
    print("You have decided to follow the ambassadors, good choice! They just left yesterday so you will likely be able to catch them. ") 
    print("Just head to Old Ashton they're sure to stock up on supplies there.")
    print("..........")
    print(" ")
    print("After an afternoon of hard riding you arrive in Old Ashton")
    print("You see a tavern, a long main road and many small alleyways and sidestreets.")
    print("The town is surround by steep hils in the back and the sea at the end of the main road.")
    print("What do you want to do?")
    print("You could check out the tavern and see if the barkeep knows anything ") 
    print("about the diplomats or look for fancy carriages that might be carrying the diplomats?")
    option = input("Type 'barkeep' to speak with the barkeep, or 'carriages' to look for the carriages. ")
    print(" ")
    if (option == "barkeep"):
        innkeeper()
    elif (option == "carriages"):
        carriages()
    else:
        print("Invalid answer, Why don't you try again?")
        goambassador()

def innkeeper():
    """The user speaks with an barkeep in this function.

    The barkeep directs the user to go to a hotel to see if the ambassadors are there.
    The user is then prompted to follow the barkeep advice or not. If they do
    not they will be sent to the carriages option.
    Depending on the users choice a different function is called.
    """
    print(" ")
    print("You enter the tavern and head to the counter. There an old man is standing ")
    print("behind the bar washing mugs. You go up and say hello, flash a couple coins ")
    print("and ask if he knows anything about a group of ambassadors that may have ")
    print("stopped in recently.")
    ##fix this in github
    print("The barkeep looks at the coins and tells you that you might have better")
    print("luck at the inn on the outskirts of town. He then winks and takes your gold. ")
    print("Would you like to follow up on the barkeeps advice?")
    option = input("Type 'yes' to go to the inn or 'no' to try looking for the carriages instead. ")
    print(" ")
    if (option == "yes"):
        yeshotel()
    elif (option == "no"):
        carriages()
    else:
        print("Invalid answer, Why don't you try again?")
        innkeeper()

def yeshotel():
    """This function takes the user to a hotel.

    The user goes to the hotel and sees the ambassadors.
    The user is then prompted to go up to the ambassadors and speak with them
    or spy on them instead.    
    Depending on the users choice a different function is called.
    """
    print(" ")
    print("You arrive at the large surprisingly fancy inn and find the ")
    print("ambassadors sitting in the restaurant below. ")
    print("Do you go up to speak with them or stay hidden and spy on them?")
    option = input("Type 'spy' to spy on them or 'talk' to speak with them. ")
    print(" ")
    if (option == "spy"):
        spyambassador()
    elif (option == "talk"):
        talkambassador()
    else:
        print("Invalid answer, Why don't you try again?")
        yeshotel()

def spyambassador():
    """This function allows the user to spy on the ambassadors.

    The user stays hidden to watch the ambassadors in this function to discover
    any information about the stolen jewel. They see an ambassador leave the group
    and are given the choice to follow the lone ambassador or stay where they are.
    Depending on the users choice a different function is called.
    """
    print(" ")
    print("You sit down strategically concealed from view but with a good sight of the ambassadors. ")
    print(" After a few minutes you see one ambassador leave the group and ") 
    print("walk hurriedly towards the stables while the others are distracted")
    print(" ")
    print("What should you do? Follow the ambassador or stay and watch the others? ")
    option = input("Type 'stay' to stay, or 'follow' to follow. ")
    print(" ")
    if (option == "stay"):
        stayambassador()
    elif (option == "follow"):
        followambassador()
    else:
        print("Invalid answer, Why don't you try again?")
        spyambassador()

def stayambassador():
    """This function allows the user to stay and watch the ambassadors.

    The user eventually gets bored and goes up to speak with the ambassadors.
    In the course of the conversation the user is prompted to bring up the missing
    jewel or not.    
    Depending on the users choice a different function is called.
    """
    print(" ")
    print("The other ambassador doesn't come back and the others show no sign of moving")
    print("After another hour you get bored and go up to the ambassadors. ")
    print(" ")
    print("They welcome you as a fellow traveler and begin to tell you about the ball ")
    print("and their travels. ")
    print("Now might be your chance to find something out. Do you bring up the missing jewel?")
    option = input("Type 'yes' to ask what they know about the jewel, or 'no' to leave and find the the other diplomat. ")
    print(" ")
    if (option == "yes"):
        yescontroversy()
    elif (option == "no"):
        followambassador()
    else:
        print("Invalid answer, Why don't you try again?")
        stayambassador()

def yescontroversy():
    """The user brings up the missing jewel to the ambassadors in this function.

    After bringing up the jewel one ambassador acts suspiciously. 
    The suspicious ambassador then offers the user a drink which they may take 
    or decline.
    Depending on the users choice a different function is called.
    """
    print(" ")
    print("As they continue to talk about the ball you ask whether they heard that ") 
    print("someone had stolen the princesses crown jewel after the ball. ")
    print("One of the ambassadors immediately looks away and seems to becomes very wary of you, ") 
    print("but the rest seem shocked and horrified. ")
    print("The conversation moves on from the jewel, and the ambassador that seemed ")
    print("nervous when you brought it up offers you a drink.")
    option = input("Do you accept this kind offer? Type 'yes' to accept, or 'no' to decline. ")
    print(" ")
    if (option == "yes"):
        print("Unfortunately the cup was poisoned.")
        death()
    elif (option == "no"):
        successfunction1()
    else:
        print("Invalid answer, Why don't you try again?")
        yescontroversy()

def followambassador():
    """This function allows the user to follow the ambassador that left the group.

    The user goes to the stables and finds the ambassador taking the jewel out of
    a saddle bag. They stay hidden and follow the ambassador until the user is
    prompted to confront the ambassador or continue following them.    
    Depending on the users choice a different function is called.
    """
    print(" ")
    print("You find the ambassador in the stables digging through the groups saddlebags. ")
    print("Staying out of sight you watch him take out a small pouch and quickly ")
    print("leave the stable in the direction of the town. ")
    print("You follow him from a distance as he walks quickly away from the hotel. ")
    print("Should you confront him or keep watch from a distance?")
    option = input("Type 'confront' to confront the ambassador, or 'follow' to  keep following. ")
    print(" ")
    if (option == "confront"):
        successfunction2()
    elif (option == "follow"):
        jumpdeath()
    else:
        print("Invalid answer, Why don't you try again?")
        followambassador()

def talkambassador():
    """The user sits with the ambassadors at the hotel in this function.

    The user is welcomed by the ambassadors who speak about the ball. The user is
    then asked whether they would like to bring up the jewel or leave to find the
    other diplomat who left the group earlier.
    Depending on which option the user chooses a different function is called.
    """
    print(" ")
    print("They welcome you as a fellow traveler and begin to tell you about the ball ")
    print("and their travels. ")
    print("Now might be your chance to find something out. Do you bring up the missing jewel?")
    option = input("Type 'yes' to ask what they know about the jewel, or 'no' to leave and find the the other diplomat. ")
    print(" ")
    if (option == "yes"):
        yescontroversy()
    elif (option == "no"):
        followambassador()
    else:
        print("Invalid answer, Why don't you try again?")
        talkambassador()

def carriages():
    """This function allows the user to search for the ambassadors carriages.

    The user walks through the town looking for the carriages and notices a 
    fancy building at the top of a hill near the wharf. The user is then asked 
    whether they would like to go to the fancy building or continue looking around
    the main town.
    Depending on which option the user chooses a different function is called.
    """
    print("You decide to walk along the main road to the wharf at the end. ")
    print("As you walk you look down the small side roads and alleys but see only ")
    print("small shops and houses. Most of which seem uncared for and about to fall down. ")
    print("as you continue along the road you notice a large building slightly on the ")
    print("outskirts of the town, looking out of place as the only well cared for building ")
    print("in the town. Would you like to go check it out or keep looking for the carriages. ")
    option = input("Type 'building' to check out the building, or 'continue' to keep exploring. ")
    print(" ")
    if (option == "building"):
        yeshotel()
    elif (option == "continue"):
        jumpdeath()
    else:
        print("Invalid answer, Why don't you try again?")
        carriages()

##Patrick's Code
def gorelative():
    """This is the first function for the relative option. 

    The user has multiple options to go through with the limited information at the start. 
    The user is first prompted to either a creek or staying at the location.
    Depending on which option the user chooses, a new function will be called.
    """
    print(" ")
    print("The jewel has been stolen. There is a wizard standing at the creek.")
    print("You aren’t sure where the jewel has left.")
    print("You see a jealous relative leave the party and hear he left for a creek.")
    print("You come to a creek.")
    cross = input("Type 'creek' to cross the creek or 'stay' to stay. ")
    if (cross == "creek"):
        print("You move onto the troll.")
        troll()
    elif (cross == "stay"):
        print("The wizard betrays you and kills you with a fire bolt from his wand.")
        death()
    else:
        print("Invalid answer. Why don't you try again?")
        gorelative()

def troll():
    """This is the function that leads to the troll.

    The user would move to troll after choosing the creek option. 
    The user has the option to stay with the troll or move to the dragon in the mountain.
    Depending on which option the user chooses, a new function will be called.
    """
    print("")
    print("You now meet a troll.")
    print("The troll is annoyed because you woke him up from his nap.")
    print("He asks why you woke him up from his nap.")
    print("You tell him that a wizard said he spoke with you.")
    print("The troll chortles, that fool is always getting me into trouble.")
    print("He tells you that the relative has gone near a mountain.") 
    move = input("Type 'mountain' to go to the mountain or 'stay' to stay with the troll. ")
    if (move == "stay"):
        print("The troll doesn't like you staying, so he eats you.")
        death()
    elif (move == "mountain"):
        dragon()
    else:
        print("Invalid answer. Why don't you try again?")
        troll()

def dragon():
    """This is the function that leads to the dragon.

    The user would move onto the dragon after receiving the options from the troll.
    The user would either stay with the dragon or proceed to the phoenix.
    Depending on which option the user chooses, a new function will be called.
    """
    print("")
    print("You go to a mountain, where you meet a dragon.")
    print("The dragon is famished and hasn't eaten in months.")
    print("The dragon is curious why you got so close to his mountain.")
    print("The dragon is impressed by your courage and decides to help.")
    print("He tells you that the relative has visited a phoenix.")
    print("The dragon does not like like you sticking around the mountain.")
    print("The longer you stay with the dragon, the hungrier he gets.")
    move = input("Type 'phoenix' to move onto the phoenix or 'stay' to stay with the dragon. ")
    if (move == "stay"):
        print("The dragon doesn't like you staying so he eats you.")
        death()
    elif (move == "phoenix"):   
        phoenix()
    else:
        print("Invalid answer. Why don't you try again?")
        dragon()

def phoenix():
    """This function leads to the phoenix.

    The user would move onto the phoenix after receiving the options from the dragon.
    The user would either stay with the phoenix or move onto the town.
    Depending on which option the user chooses, a new function will be called.
    """
    print("")
    print("You go to a misty woods, where you meet a phoenix.")
    print("The phoenix is frightened that you surprised him.")
    print("WOOOOOSH.")
    print("The phoenix bursts into flames, but is reborn from his ashes anew.")
    print("The phoenix is happy for company.")
    print("The phoenix dislikes the dragon you previously met.")
    print("The phoenix wishes to stay clear from his mountain.")
    print("The phoenix is more than happy to help with your quest.")
    print("The phoenix tells you the relative has gone to town.")
    move = input("Type 'town' to proceed to the town or 'stay' to stay with the phoenix. ")
    if (move == "stay"):
        print("The phoenix feels threatened, so he lights you on fire.")
        death()
    elif (move == "town"):
        town()
    else:
        print("Invalid answer. Why don't you try again?")
        phoenix()

def town():
    """This function leads to the town and the end of this storyline.

    The user learns from the dialogue in the town about the other storyline's options.
    The user finally meets the jealous relative.
    The user has the option to either stay with the relative or meet the diplomats.
    Depending on which option the user chooses, a new function will be called.
    """
    print("")
    print("You go to the town, where you finally meet the relative.")
    print("The relative is angered that you thought he would steal the jewel.")
    print("Relative: That's very rude of you to think that I have the jewel.")
    print("Relative: I don't have the jewel, I heard that it was in a hotel, with some foreign diplomats.")
    move = input("Type 'go' to move to the hotel or 'stay' to stay with the relative. ")
    if (move == "stay"):
        print("The relative kills you since you thought he stole the jewel.")
        death()
    elif (move == "go"):
        yeshotel()
    else:
        print("Invalid answer. Why don't you try again?")
        town()

##Natalie's Code
def gomage():
    """This is the first function for the mage option.

    This function starts the user on a quest to find the mage. The user is 
    prompted to with the choice of either crossing a river or going down a path.
    Depending on which option the user chooses a different function is called.
    """
    print("")
    print("You picked to go after the mage. A guard noticed that the mage ran off towards a tower in the distance.")
    print("You come across a decrepit bridge that runs across a fast flowing river.")
    print("If you cross the river it cuts down the time to the mage, but you risk falling. There is also a path around the river that takes you longer.")
    cross = input("Type 'river' to cross the river or type 'path' to follow the path. ")
    if (cross == "river") :
        print("")
        print("Oh no! The wooden plank breaks underneath you and you fall to your death!")
        death()
    elif (cross == "path"):
        path()
    else:
        print("Invalid answer. Why don't you try again?")
        gomage()

def path():
    """This function leads the user down a path.

    The user walks down a path to a town. The user is 
    prompted to to either talk to a guard or woman at the town entrance.
    Depending on which option the user chooses a different function is called.
    """
    print("")
    print("As you walk across the path you come across a town.")
    print("Outside of the town you see a guard and a old woman. Maybe one of them knows where the mage is.")
    town = input("Type 'guard' talk to the guard or 'woman' to talk to the woman. ")
    if (town == "guard") :
        guard()
    elif (town == "woman") :
        woman()
    else:
        print("Invalid answer. Why don't you try again?")
        path()
        
def guard():
    """The user talks to a guard in this function.

    The user talks to a guard to find where the mage is. The user is 
    prompted then is promoted to go to the tower where the guard is or to talk to
    the woman.
    Depending on which option the user chooses a different function is called.
    """
    print("")
    print("You approach the guard.")
    look = input("Guard: who are you looking for? ")
    print("Guard: I heard the "+look+" is located in a tower just outside of town. That is the best place to look for him")
    print("Guard: I need to get back to work. Now get out of here!")
    print("You are now walking away from the gaurd. Do you want to talk to the woman or search for the tower?")
    search = input("Type 'woman' to talk to the woman or type 'tower' to go to the tower. ")
    if (search == "woman") :
        woman()
    elif (search == "tower") :
        ##need to do print
        tower()
    else:
        print("Invalid answer. Why don't you try again?")
        guard()

def woman():
    """The user talks to a woman in this function.

    The user talks to a woman to find where the mage is. The user is 
    prompted then is promoted to go to the tower where the mage is is or to talk
    to the guard.
    Depending on which option the user chooses a different function is called.
    """
    print("")
    look = input("Woman: hello traveler, who are you looking for? ")
    print("Woman: I heard the "+look+" is located in a tower just outside of town.")
    print("Woman: I would hurry though because the mage might leave soon.")
    print("You are now walking away from the woman. Do you want to talk to the guard or search for the tower?")
    tw = input("Type 'guard' to talk to the woman or type 'tower' to go to the tower. ")
    if (tw == "tower") :
        tower()
    elif (tw == "guard") :
        guard()
    else:
        print("Invalid answer. Why don't you try again?")
        woman()

def tower():
    """The user enters the tower and chooses a direction to explore.

    The user enters the tower and sees a staircase. The user is 
    then promoted to go either go up or down the stairs.
    Depending on which option the user chooses a different function is called.
    """
    print("")
    print("as you approach the tower you notice that the door is open and you go inside.")
    print("once inside you see a stairwell")
    stairs = input("Type 'up' to go up the stairs or type 'down' to go down the stairs. ")
    if (stairs == "up") :
        up()
    elif (stairs == "down") :
        print("Oh no! It looks like there was a trap door in the stairs. You fall to your death.")
        death()
    else:
        print("Invalid answer. Why don't you try again?")
        tower()

def up(first=True):
    """The user goes up the stairs and picks which door to enter.

    The user climbs up the stairs to the halways. The user is 
    then promoted to either go into room one or room two.
    Depending on which option the user chooses a different function is called.

    parameters
    ---------
    Boolean

    Calling this function for the first time results in the user being in the
    hallway for the first time. If the user calls the function again after going
    into the first room, they are prompted to go into the second room.
    """
    if first == True:
        print("At the top of the stairs you notice two doors")
        doors = input("Type 'one' to go into the first room or 'two' to go into the second room. ")
    if first == False:
        print("You are back at the hallway and start to open door two")
        two()
    if (doors == "one") :
        print("this room is empty, please return to the hallway")
        up(False)
    elif (doors == "two") :
        two()
    else:
        print("Invalid answer. Why don't you try again?")
        up(False)

def two():
    """The user enters room two and talks with the mage.

    The user enters room two and talks with the mage. The mage tells the user 
    that he does not have the jewel and to look for the ambassador. The user is 
    then promoted to go to the town.
    Depending on which option the user chooses a different function is called.
    """
    print("")
    print("As you open the door you notice the mage is sitting in the chair")
    why = input("Mage: why have you come here? ")
    print("Mage: I do not have the "+why+" that you are looking for.")
    print("Mage: I did see the ambassador with the "+why+" when I passed through the town. Maybe look there?")
    goback = input("Type 'yes' to go into the town or 'no' to not go to the town. ")
    if (goback == "yes"):
        sign()
    elif (goback == "no"):
        print("it seems like the jewel is in the town, maybe you should reconsider")
        sign()
    else:
        print("Invalid answer. Why don't you try again?")
        two()
def sign():
    """The user returns to the town to look for the ambassador.

    After finding out that the mage nor the relative has the jewel, the user is 
    told to search for the ambassador. This function brings the user back to the 
    town. The user talks to the man who tells the user that the ambassador is in
    the htoel. The user is then promptoed to go to the hotel.
    Depending on which option the user chooses a different function is called.
    """
    print("You are now back in the town and are approached by a man")
    print("")
    look = print("Man: you look lost Friend, who are you looking for? ")
    print("Man: I saw the "+look+" went into the hotel over there!")
    option = input("Type 'yes' to go to the hotel or 'no' to not go to the hotel. ")
    if (option == "yes"):
      yeshotel()
    elif (option == 'no'):
      print("Man: what are you still doing here? You should get to the hotel before it is too late.")
      print("You now proceed to the hotel")
      yeshotel()
    else:
      print("Invalid answer, why don't you try again?")
      sign()

##death functions
def death():
    """This is a general death function for when the user dies.

    If a user chooses a function that results in their death then this function
    is called. The user is then asked if they would like to start the game over
    or if they want to end the game.
    Depending on which option the user chooses a different function is called.
    """
    print("This option has resulted in your death.")
    print("Would you like to play again? Type 'yes'")
    option = input("Would you like to play again? Type 'yes' to start over, or 'no' to end the game. ")
    if (option == "yes"):
        start()
    elif (option == "no"):
        endgame()
    else:
      print("Invalid answer, why don't you try again?")
      death()

#Specific death function
def jumpdeath():
    """This is a specific death function for when the user dies in the ambassador
     branch.

    If the user chooses a incorrectly when following the ambassador or
    looking for the carriages the user will be sent to this death function. The 
    user is then asked if they would like to begin again or end the game.
    Depending on which option the user chooses a different function is called.
    """
    print(" ")
    print("as you continue through a dark alley you hear something behind you.")
    print("you trun around just in time to see a group of bandits closing in on and as you begin to run, ")
    print("you wonder are these the culprits?")
    print("unfortuenately you will never know because just as you see a larger road one of the bandits comes ")
    print("out from in front blocking your escape, and the rest close in from behind. ")
    print(" ")
    print("Game over.")
    print("You have been killed.")
    print(" ")
    option = input("Would you like to play again? Type 'yes' to start over, or 'no' to end the game. ")
    if (option == "yes"):
        start()
    elif (option == "no"):
        endgame()
    else:
        print("Invalid answer, Why don't you try again?")
        jumpdeath()

##success funtion
def successfunction1():
    """This is the first success function.
    
    The function occurs when the user correctly refuses to drink the wine offered
    by the suspicious ambassador. The user is then asked if they would like to begin 
    again or end the game.
    Depending on which option the user chooses a different function is called.
    """
    print(" ")
    print("The ambassador becomes immediately offended and asks why you have refused the wine. ")
    print("You respond by telling him that you believe he is not to be trusted and also that you think he ")
    print("knows something about the missing jewel.")
    print("Surprisingly the ambassador caves quickly and admits to the theft.")
    print("You ask where the jewel is and it turns out he has kept it in his pocket, much to the shock of his compatriots. ")
    print(" ")
    print("Good work! You have found the jewel and can return it to the palace")
    option = input("Would you like to play again? Type 'yes' to start over, or 'no' to end the game. ")
    print(" ")
    if (option == "yes"):
        start()
    elif (option == "no"):
        endgame()
    else:
        print("Invalid answer, why don't you try again?")
        successfunction1()

def successfunction2():
    """This is the second success function.

    The function occurs when the user decides to confront the ambassador who left
    the larger group. The user is then asked if they would like to begin 
    again or end the game.
    Depending on which option the user chooses a different function is called.
    """
    print(" ")
    print("The ambassador had no idea he was being followed and is easily overpowered. ")
    print("You demand to know where the jewel is and he shows you the pouch. ")
    print("Good work! You have found the jewel and can return it to the palace! ")
    option = input("Would you like to play again? Type 'yes' to start over, or 'no' to end the game. ")
    print(" ")
    if (option == "yes"):
        start()
    elif (option == "no"):
        endgame()
    else:
        print("Invalid answer, Why don't you try again?")
        successfunction2()

#end function
def endgame():
  """This is the function that ends the game.

    There are no prompts, only a line of text thanking the user for playing.
    """
  print("")
  print("Thank you for playing")

##start function
def start():
    """This is the function that starts the game.

    The user is prompted to enter their name into the game. Then the function 
    calls the introduction functions to begin the choose your own adventure game.
    """
    name = input("What's your name? ")
    start()
    print("")
    print("Welcome to your adventure")
    print("")
    print("Your name is "+name+", and you're a poor peasant who's trying to find a stolen jewel.")
    intro()
