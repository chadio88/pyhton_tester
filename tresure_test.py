display_inventory={'arrow':12,'gold coin':42,'rope':1,'torch':6,'dagger':1,}
for k in display_inventory.items():
  print('Key: ' + str(k))
print(list(display_inventory.keys()))
print(list(display_inventory.values()))
print('arrow' in display_inventory.keys())
dis=display_inventory={'arrow':12,'gold coin':42,'rope':1,'torch':6,'dagger':1}
print('You have ' + str(dis.get('arrow',0)) + ' arrows.')
print(dis['arrow'])
message='long live the fighters, the sleeper must awaken'
count={}
for character in message:
  count.setdefault(character,0)
  count[character]=count[character] + 1
print(count)
def inventory_display(inventory):
  print('Inventory:\n')
  for k,v in dis.items():
    print(str(v) +  ' '  + k)
  total=sum(dis.values())
  print('\nToal number of items: ' + str(total))
inventory_display(dis)
dragon_loot=['gold coin','gold coin','ruby','dagger','gold coin','ruby']
new_loot={}
def con_inventory(inventory):
  for i in range(len(dragon_loot)):
    new_loot[dragon_loot[i]]=dragon_loot.count  (dragon_loot[i])
  print(new_loot)
con_inventory(dragon_loot)
def add_inventory(inventory, added_items):
  for i in range(len(dragon_loot)):
    if dragon_loot[i] in dis:
      dis[dragon_loot[i]]=dis[dragon_loot[i]]+1
    else:
      dis[dragon_loot[i]]=1
  print(dis)
  inventory_display(dis)
add_inventory(dis,dragon_loot)


