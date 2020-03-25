
# learning git

import random

def play1():
  coin=[]
  x=0
  y=0
  i=1
  while i<=10000:
    flip=random.randint(0,1)
    if flip==0:
      coin.append('H')
      x=x+1
    else:
      coin.append('T')
      y=y+1
    i=i+1
  print(coin)
  print(x, 'Heads')
  print(y, 'Tails')

  toss=''.join(coin)
  print(str(toss.count('HHH')/10000*100) + ' %')

def play3():
  import treasure_test

def play2():
  import zombie_dice

play3()




