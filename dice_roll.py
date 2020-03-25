import random


class Dice:
  def roll(self):
    first=random.randint(1,6)
    second=random.randint(1,6)
    return first,second


x=1
for x in range(1):   
  dice=Dice()
  print(dice.roll())
