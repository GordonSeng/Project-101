import random

def print_dice(dice_roll):
  if dice_roll == 1:
    print(" ----- ")
    print("|     |")
    print("|  0  |")
    print("|     |")
    print(" ----- ")
  elif dice_roll == 2:
    print(" ----- ")
    print("| 0   |")
    print("|     |")
    print("|   0 |")
    print(" ----- ")
  elif dice_roll == 3:
    print(" ----- ")
    print("|     |")
    print("|0 0 0|")
    print("|     |")
    print(" ----- ")
    print(" ----- ")
  elif dice_roll == 4:
    print("| 0 0 |")
    print("|     |")
    print("| 0 0 |")
  elif dice_roll == 5:
    print(" ----- ")
    print("| 0  0 |")
    print("|   0  |")
    print("| 0  0 |")
    print(" ----- ")
  elif dice_roll == 6:
    print(" ----- ")
    print("| 0 0 0 |")
    print("|       |")
    print("| 0 0 0 |")
    print(" ----- ")

response = "y"

while response == "y":
  no = random.randint(1, 6)

  print_dice(no)

  response = input("Press 'y' to roll again or 'n' to exit: ")

print("Thanks for playing!")