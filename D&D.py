import secrets


class Character:

    player = ""
    playclass = ""
    race = ""

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
    playclass_verify = False
    playclass = 0
    while not playclass_verify:
        input_playclass = input("Input class number >>")
        if not input_playclass:
            print("Come on, it's not that hard choosing a class!")
        else:
            playclass = int(input_playclass)
            if playclass > 1 or playclass < 1:
                print("We don't have that class yet, or it doesn't exist.")
            else:
                playclass_verify = True

    if playclass == 1:
        c.playclass = "Barbarian"

    print("Next step! It's time for the race, let's see what have you thought of.")
    print("1. Human")
    playrace_verify = False
    playrace = 0
    while not playrace_verify:
        input_playrace = input("Input race number >>")
        if not input_playrace:
            print("Your character doesn't exist? It needs to be something!")
        else:
            playrace = int(input_playrace)
            if playrace > 1 or playrace < 1:
                print("We don't have that race yet, or it doesn't exist.")
            else:
                playrace_verify = True
    
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
    rollchoose_verify = False
    rollchoose = 0
    while not rollchoose_verify:
        input_rollchoose = input("Input rolls number >>")
        if not input_rollchoose:
            print("Choose one, don't be shy.")
        else:
            rollchoose = int(input_rollchoose)
            if rollchoose > 3 or rollchoose < 1:
                print("Wrong choice! Please go again.")
            else:
                rollchoose_verify = True
    
    finalrolls = currentrolls[rollchoose-1]
    print(finalrolls)

    c.sofar()


if __name__ == "__main__":
    main()
