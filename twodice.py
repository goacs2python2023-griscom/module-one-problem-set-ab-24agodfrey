import random

def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    if dice_sum in [6, 7, 8]:
        return "win"
    else:
        return "lose"

print(roll_dice())