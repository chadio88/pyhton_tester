
import random

dice_can=['green','green','green','green','green','green','yellow','yellow','yellow','yellow','red','red','red']

green_die=['gbrains','gbrains','gbrains','gfoot','gfoot','gshot']
yellow_die=['ybrains','ybrains','yfoot','yfoot','yshot','yshot']
red_die=['rbrains','rfoot','rfoot','rshot','rshot','rshot']

live_humans=3
rand_roll=random.choices(dice_can,k=live_humans)
print(rand_roll)

brains=0
shots=0
dice_can=['green','green','green','green','green','green','yellow','yellow','yellow','yellow','red','red','red']
first_roll=[]

for i in range(0,3):
  if rand_roll[i]=='green':
    dice_can.remove('green')
    first_roll.append(random.choice(green_die))
  elif rand_roll[i]=='yellow':
    dice_can.remove('yellow')
    first_roll.append(random.choice(yellow_die))
  else:
    rand_roll[i]=='red'
    dice_can.remove('red')
    first_roll.append(random.choice(red_die))
print('can: ', dice_can)
dice=first_roll


while shots<3:
  def totals():
    global brains, shots
    m=[]
    for i in range(0,3):
      if dice[i]=='gbrains' or dice[i]=='ybrains' or dice[i]=='rbrains':
        brains=brains+1
      elif dice[i]=='gshot' or dice[i]=='yshot' or dice[i]=='rshot':
        shots=shots+1
      elif dice[i]=='gfoot':
        m.append(random.choice(green_die))
        if 'gshot' in m:
          shots=shots+1
        elif 'gbrains' in m:
          brains=brains+1
      elif dice[i]=='yfoot':
        m.append(random.choice(yellow_die))
        if 'yshot' in m:
          shots=shots+1
        elif 'ybrains' in m:
          brains=brains+1
      else:
        dice[i]=='rfoot'
        m.append(random.choice(red_die))
        if 'rshot' in m:
          shots=shots+1
        elif 'rbrains' in m:
          brains=brains+1
    print('Brains: ' + str(brains)) 
    print('Shots: ' + str(shots))
    return m


  def next_roll():
    rand_reroll=random.choices(dice_can,k=3-len(m))
    print(rand_reroll)
    p=[]
    for i in range(0,3-len(m)):
      if rand_reroll[i]=='green':
        dice_can.remove('green')
        p.append(random.choice(green_die))
      elif rand_reroll[i]=='yellow':
        dice_can.remove('yellow')
        p.append(random.choice(yellow_die))
      else:
        rand_reroll[i]=='red'
        dice_can.remove('red')
        p.append(random.choice(red_die))
    return p 


  def debug(*args):
    if True:
      print('DEBUG:', *args)

  debug("dice:", dice)
  m=totals()
  debug(m)
  p=next_roll()
  debug("Next roll:", p + m)
  print("can:", dice_can)
  dice=p+m
