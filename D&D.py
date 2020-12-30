import secrets


class Character:

    player = ""
    playclass = ""
    race = ""

    strength = 0
    dexterity = 0
    constitution = 0
    wisdom = 0
    intelligence = 0
    charisma = 0

    def __init__(self, player):
        self.player = player

    def sofar(self):
        print("Your name is " + self.player + ", and your class is " + self.playclass)


def rolldices():
    rolls = [0,0,0]
    i = 0
    while (i < 3):
        rolls[i] = secrets.randbelow(6)+1
        i = i + 1
    minroll = 6
    suma = 0
    for roll in rolls:
        suma += roll
        if roll < minroll:
            minroll = roll
    suma -= minroll
    return suma


def modifier(stat):
    return (stat - 10) / 2

def getinput(amount):
    verify = False
    num = 0
    while not verify:
        inputter = input(">>")
        if not inputter:
            print("Error: empty input. Try again!")
        else:
            num = int(inputter)
            if (num < 1 or num > amount):
                print("Error: invalid input. Try again!")
            else:
                verify = True
    return num

def main():
    print("Welcome to the D&D Character creator V 0.1! Let's get started, shall we?")
    print("First of, what is your name? (the player, not the character)")
    player = input(">>")
    while not player:
        if not player:
            print("You gotta identify yourself, y'know?")
            player = input(">>")

    c = Character(player)

    print("Good! Now that that's out of the way, let's go with your class. What do you want to play today?")
    print("1. Barbarian")
    playclass = getinput(1)

    if playclass == 1:
        c.playclass = "Barbarian"

    print("Next step! It's time for the race, let's see what have you thought of.")
    print("1. Human")
    playrace = getinput(1)
    
    if playrace == 1:
        c.race = "Human"

    print("And now, it's time for the dice rolls! These will be fully automated, so just sit back and- oh, they're done already? Have a look!")
    currentrolls = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    i = 0
    while (i < 6):
        currentrolls[0][i] = rolldices()
        currentrolls[1][i] = rolldices()
        currentrolls[2][i]= rolldices()
        i += 1
    
    print(currentrolls[0])
    print(currentrolls[1])
    print(currentrolls[2])

    print("So... Which one do you prefer?")
    rollchoose = getinput(3)
    
    finalrolls = currentrolls[rollchoose-1]
    print(finalrolls)

    c.sofar()


if __name__ == "__main__":
    main()
