# Sexy Password
import random

adjective_list=['bloody','black','purple','hairy','dirty','tiny','huge','brown']
# adjective = random.choice(adjective_list)
random.shuffle(adjective_list)
adjective=adjective_list[0]
print('The sexy password is ' + adjective + '_____?')
password_list=['cunt','dick','vagina','asshole','titties','penius','clit','cock']
random.shuffle(password_list)
password=password_list[0]
guess_count=0
while guess_count<3:
  guess=input('Guess, you sexy beast: ')
  if guess==password:
    print(adjective + ' ' + password)
    print('Very nice guess! You Perve!')
    break
  elif guess!=password:
    print(adjective + ' ' + guess)
    print('Very naughty guess!')
  guess_count+=1
else:
  print('The sexy password was: ' + adjective + ' ' + password + '!')


