import random


spam=['apples','bananas','grapes']
def banana_game():
  a=0
  while a<3:
    roll=random.choices(spam,k=3)
    print(roll)
    m=[]
    for i in range(0,3):
      if roll[i]=='apples':
        print('A')
        a=a+1
      elif roll[i]=='bananas':
        print('B')
        m.append(random.choice(spam))
      else:
        print('G')
    print(m)
  return m

m=banana_game()

  
  