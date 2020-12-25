import random

class Character:

    player = ""
    playclass = ""
    race = ""

    def __init__(self, player):
        self.player = player

    def sofar(self):
        print("Your name is " + self.player + ", and your class is " + self.playclass)

def rolldices():
    rolls = []
    i = 0
    while (i < 4):
        rolls[i] = random.randint(1,6)
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

print("Welcome to the D&D Character creator V 0.1! Let's get started, shall we?")
print("First of, what is your name? (the player, not the character)")
player = input(">>")
while not player:
    if not player:
        print("You gotta identify yourself, y'know?")
        player = input()

c = Character(player)

print("Good! Now that that's out of the way, let's go with your class. What do you want to play today?")
print("1. Barbarian")
playclass_verify = False
playclass = 0
while not playclass_verify:
    input_playclass = input("Input number >>")
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

c.sofar()