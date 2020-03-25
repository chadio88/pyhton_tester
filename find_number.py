def find_phone(text):
  if len(text)!=12:
    return False
  for i in range(0,3):
    if not text[i].isdecimal():
      return False
  if text[3]!='-':
    return False
  for i in range(4,7):
    if not text[i].isdecimal():
      return False
  if text[7]!='-':
    return False
  for i in range(8,12):
    if not text[i].isdecimal():
      return False
    return True
print('Is the number 480-285-4370 is a real phone number?')
print(find_phone('480-285-4370'))
print('Is RachelRachel a real phone number?')
print(find_phone('RachelRachel'))
