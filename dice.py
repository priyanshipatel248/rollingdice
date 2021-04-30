import itertools
import random


# Roll_function
def roll_dice():
    dice_no = list(range(1, 7))
    combination = list(itertools.product(dice_no, repeat=2))
    rolled_dice = random.choice(combination)
    input("press any key to roll")
    print("your dice is {0}".format(rolled_dice))

while True:
  roll_dice()
  again=input("roll  again? yes/no")
  if again=="no":
    print("Exisiting...")
    break

