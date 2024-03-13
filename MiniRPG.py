import random
Char = input('Write the name of your character:')
MaxHealth = 10
Health= 10
lvlupreq = 20
lvl = 1
xp = 0
swdmg = random.randint(2, 3)
shiprot = 1
print(f'Welcome to the game {Char}!, you start with {Health} health points, and you are level {lvl}. Also, you start with a sword and a shield.')
print('')
print(f' Now that you´ve already woken up near a cliff,')
print(f' you see that there are three places you can go.')
print('')
print('     Where do you want to go?')
print('')
print('1. The forest')
print('2. The beach')
print('3. The city')
print('')
Dec = int(input('Write the number of the place you want to go: '))
if Dec == 1:
    print('You are in the forest, you see a witch, what do you do?')
    print('1. Go away quietly')
    print('2. Fight')
    print('3. Try to be friends')
    Dec1 = int(input(f'Write the number of the action you want to do {Char}: '))
    if Dec1 == 1:
        print('You go away quietly depper into the forest')
    elif Dec1 == 2:
            print('You start the fight with the witch')
            witchH = 10
            witchAtk = random.randint(1, 3)
            print(f'You have {Health} health points')
            print(f'The witch has 10 health points')
            print('')
            
            while Health != 0 and witchH > 0 and Dec1 != 3:
                print('1. Attack')
                print('2. Defend')
                print('3. Run')
                Dec1 = int(input('Write the number of the action you want to do: '))

                if Dec1 == 1:
                        print('You attack the witch')
                        witchH = witchH - swdmg
                        print(f'The witch has {witchH} health points')
                        print('')
                        print('The witch attacks you')
                        Health = Health - witchAtk
                        print(f'You have {Health} health points')
                        print('')
                elif Dec1 == 2:
                        print('You defend yourself')
                        print('The witch attacks you')
                        Health = Health - witchAtk + shiprot
                        print(f'You have {Health} health points')
                        print('')
                elif Dec1 == 3:
                        print('You run away')
                        Health = Health - 2
                else:
                    print('Write a valid number')
                        
            if Health > 0:
                print('You have defeated the witch')
                xp = xp + random.randint(8, 13)
                print(f'You have {xp} experience points')
                print('')
                print('You continue your journey deeper in the forest')
            elif Health == 0 or Health <=0 and Dec1 != 3:
                print('You have been defeated by the witch')
                print(f'Game Over {Char} :(')
            elif Dec1 == 3 and Health > 0:
                print(f'You run away from the witch and you have {Health} health points left')
                print('You continue your journey deeper in the forest')
    elif Dec1 == 3:
        print('You try to be friends with the witch, but she doesn´t want to be friends with you and hits you with a spell')
        print(f'You continue your journey deeper in the forest and lose 2 health points and gain some experience points')
        xp = xp + random.randint(2, 6)
        Health = Health - 2
        print(f'You have {Health} health points and {xp} experience points')  
    else:
        print('Write a valid number')
elif Dec == 2:
     print('You are in the beach, you see a house in the distance, what do you do?')
     print('   1. Approach the house')
     print('   2. Stay in the beach')
     print('   3. Go swimming')
     Dec2 = int(input(f'Write the number of the action you want to do {Char}: '))
     if Dec2 == 1:
        print('You approach the house and suddenly you remember "Oh thats´s my house!"')
        print('and you stay there living happily ever after :)')
        print('The end')
     elif Dec2 == 2:
          print('You stay in the beach and enjoy the view')
          print('You gain 2 experience points')
          xp = xp + 2
          print('The end :)))')
     elif Dec2 == 3:
          print('You go swimming and a random rock hits you')
          print('You lose 2 health points and gain some experience points')
          xp = xp + random.randint(3, 5)
          Health = Health - 2
          print(f'You have {Health} health points and {xp} experience points')
          print('Now you go deeper into the ocean and you see a treasure chest in a hidden shipwreck inside a cave, what do you do?')
          print('1. Go to the chest')
          print('2. Go inside a hole in the cave')
          Dec3 = int(input(f'Write the number of the action you want to do {Char}: '))
          if Dec3 == 1:
              print('You go to the chest and find...')
              loot = random.randint(1, 3)
              if loot == 1:
                  print('Nothing, the chest is empty :(')
                  print('You gain 5 experience points')
                  xp = xp + 5
                  print(f'You have {xp} experience points')
              elif loot == 2:
                    print('A magic sword and a magic shield')
                    print('You gain 3 experience points')
                    swdmg = swdmg + 2
                    shiprot = shiprot + 2
                    xp = xp + 10
                    print(f'You have {xp} experience points')

              else:
                  print('A magic book that gives you 14 experience points')
                  print('You gain 10 experience points')
                  xp = xp + 10
                  print(f'You have {xp} experience points')
                  
          elif Dec3 == 2:
                print('You go inside the hole and find a giant crab, what do you do?')
                crabH = 10
                crabdmg = random.randint(1, 2)
                print('1. Attack')
                print('2. Go away')
                print('3. Tell him a joke')
                Dec4 = int(input('Write the number of the action you want to do: '))
                while Health != 0 and crabH > 0 and Dec4 != 3:
                    print('1. Attack')
                    print('2. Defend')
                    print('3. Run')
                    Dec4 = int(input('Write the number of the action you want to do: '))

                    if Dec4 == 1:
                        print('You attack the giant crab')
                        crabdmg = crabdmg - swdmg
                        print(f'The giant crab has {crabH} health points')
                        print('')
                        print('The giant crab attacks you')
                        Health = Health - crabdmg
                        print(f'You have {Health} health points')
                        print('')
                    elif Dec4 == 2:
                        print('You defend yourself')
                        print('The giant crab attacks you')
                        print(f'The giant crab has {crabH} health points')
                        Health = Health - crabdmg + shiprot
                        print(f'You have {Health} health points')
                        print('')
                    elif Dec4 == 3:
                        print('You run away')
                        Health = Health - random.randint(1, 3)
                    else:
                        print('Write a valid number')
                        
                if Health > 0:
                    print('You have defeated the giant crab')
                    xp = xp + random.randint(8, 13)
                    print(f'You have {xp} experience points')
                    print('')
                    if xp >= lvlupreq:
                        lvl = lvl + 1
                        Health = MaxHealth + 3
                        swdmg = swdmg + 1
                        shiprot = shiprot + 1
                        print(f'You have leveled up to level {lvl}')
                        print(f'You have {Health} health points')
                        print(f'You have {swdmg} attack points')
                        print(f'You have {shiprot} defense points')
                        print(f'You have {xp} experience points')
                        print('You get out of the cave and go to a ship that is near the beach')
                elif Health == 0 or Health <=0 and Dec3 != 3:
                    print('You have been defeated by the giant crab')
                    print(f'Game Over {Char} :(')
                elif Dec2 == 3 and Health > 0:
                    print('')
                    crabdec = random.randint(1, 2)
                    if crabdec == 1:
                        print('The giant crab laughs and gave you... 2 experience points')
                        print(f'You run away from the giant crab and you have {Health} health points left')
                        if xp >= lvlupreq:
                            lvl = lvl + 1
                            Health = MaxHealth + 3
                            swdmg = swdmg + 1
                            shiprot = shiprot + 1
                            print(f'You have leveled up to level {lvl}')
                            print(f'You have {Health} health points')
                            print(f'You have {swdmg} attack points')
                            print(f'You have {shiprot} defense points')
                            print(f'You have {xp} experience points')
                            print('You get out of the cave and go to a ship that is near the beach')
                        else:
                            print('You get out of the cave and go to a ship that is near the beach')
                    elif crabdec == 2:
                        print('The giant crab laughs at you and hits you with a claw')
                        Health = Health - 2
                        print(f'You run away from the giant crab and you have {Health} health points left')
                        if xp >= lvlupreq:
                            lvl = lvl + 1
                            Health = MaxHealth + 3
                            swdmg = swdmg + 1
                            shiprot = shiprot + 1
                            print(f'You have leveled up to level {lvl}')
                            print(f'You have {Health} health points')
                            print(f'You have {swdmg} attack points')
                            print(f'You have {shiprot} defense points')
                            print(f'You have {xp} experience points')
                            print('You get out of the cave and go to a ship that is near the beach')
                        else:
                            print('You get out of the cave and go to a ship that is near the beach')
                
          print('Then, you go inside the hole and find a giant crab, what do you do?')
          crabH = 10
          crabdmg = random.randint(1, 2)
          print('1. Attack')
          print('2. Go away')
          print('3. Tell him a joke')
          Dec5 = int(input('Write the number of the action you want to do: '))
          while Health != 0 and crabH > 0 and Dec5 != 3:
                    print('1. Attack')
                    print('2. Defend')
                    print('3. Run')
                    Dec4 = int(input('Write the number of the action you want to do: '))

                    if Dec5 == 1:
                        print('You attack the giant crab')
                        crabH = crabH - swdmg
                        print(f'The giant crab has {crabH} health points')
                        print('')
                        print('The giant crab attacks you')
                        Health = Health - crabdmg
                        print(f'You have {Health} health points')
                        print('')
                    elif Dec5 == 2:
                        print('You defend yourself')
                        print('The giant crab attacks you')
                        print(f'The giant crab has {crabH} health points')
                        Health = Health - crabdmg + shiprot
                        print(f'You have {Health} health points')
                        print('')
                    elif Dec5 == 3:
                        print('You run away')
                        Health = Health - random.randint(1, 3)
                    else:
                        print('Write a valid number')
                        
          if Health > 0:
                    print('You have defeated the giant crab')
                    xp = xp + random.randint(8, 13)
                    print(f'You have {xp} experience points')
                    print('')
                
                    if xp >= lvlupreq:
                        lvl = lvl + 1
                        Health = MaxHealth + 3
                        swdmg = swdmg + 1
                        shiprot = shiprot + 1
                        print(f'You have leveled up to level {lvl}')
                        print(f'You have {Health} health points')
                        print(f'You have {swdmg} attack points')
                        print(f'You have {shiprot} defense points')
                        print(f'You have {xp} experience points')
                        print('You get out of the cave and go to a ship that is near the beach')
                    else:
                            print('You get out of the cave and go to a ship that is near the beach')
          elif Health == 0 or Health <=0 and Dec3 != 3:
                    print('You have been defeated by the giant crab')
                    print(f'Game Over {Char} :(')
          elif Dec2 == 3 and Health > 0:
                    print('')
                    crabdec = random.randint(1, 2)
                    if crabdec == 1:
                        print('The giant crab laughs and gave you... 2 experience points')
                        print(f'You run away from the giant crab and you have {Health} health points left')
                        if xp >= lvlupreq:
                            lvl = lvl + 1
                            Health = MaxHealth + 3
                            swdmg = swdmg + 1
                            shiprot = shiprot + 1
                            print(f'You have leveled up to level {lvl}')
                            print(f'You have {Health} health points')
                            print(f'You have {swdmg} attack points')
                            print(f'You have {shiprot} defense points')
                            print(f'You have {xp} experience points')
                            print('You get out of the cave and go to a ship that is near the beach')
                        else:
                            print('You get out of the cave and go to a ship that is near the beach')


                    elif crabdec == 2:
                        print('The giant crab laughs at you and hits you with a claw')
                        Health = Health - 2
                        print(f'You run away from the giant crab and you have {Health} health points left')
                        print('')
                        if xp >= lvlupreq:
                            lvl = lvl + 1
                            Health = MaxHealth + 3
                            swdmg = swdmg + 1
                            shiprot = shiprot + 1
                            print(f'You have leveled up to level {lvl}')
                            print(f'You have {Health} health points')
                            print(f'You have {swdmg} attack points')
                            print(f'You have {shiprot} defense points')
                            print(f'You have {xp} experience points')
                            print('You get out of the cave and go to a ship that is near the beach')
                        else:
                            print('You get out of the cave and go to a ship that is near the beach')
elif Dec == 3:
     print('Coming soon...')

          
          
          
          