from util import rolldices, modifier, InputGetter


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


def main():
    print("Welcome to the D&D Character creator V 0.1! Let's get started, shall we?")
    print("First of, what is your name? (the player, not the character)")

    name = InputGetter("You gotta identify yourself, y'know?").string()

    c = Character(name)

    print("Good! Now that that's out of the way, let's go with your class. What do you want to play today?")
    print("1. Barbarian")

    playclass = InputGetter(
        "Come on, it's not that hard choosing a class!", "We don't have that class yet, or it doesn't exist."
    ).int(1)

    if playclass == 1:
        c.playclass = "Barbarian"

    print("Next step! It's time for the race, let's see what have you thought of.")
    print("1. Human")

    playrace = InputGetter(
        "Your character doesn't exist? It needs to be something!", "We don't have that race yet, or it doesn't exist."
    ).int(1)
    
    if playrace == 1:
        c.race = "Human"

    print("And now, it's time for the dice rolls! These will be fully automated, so just sit back and- "
          "oh, they're done already? Have a look!")

    current_rolls = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    for i in range(6):
        current_rolls[0][i] = rolldices()
        current_rolls[1][i] = rolldices()
        current_rolls[2][i] = rolldices()

    for i in range(3):
        print(f"{i + 1}.", current_rolls[i])

    print("So... Which one do you prefer?")
    rollchoose = InputGetter().int(len(current_rolls))
    
    finalrolls = current_rolls[rollchoose-1]
    print(finalrolls)

    c.sofar()


if __name__ == "__main__":
    main()
