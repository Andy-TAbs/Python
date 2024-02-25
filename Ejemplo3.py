# Write code below 💖
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')
print('    2) Dusk')

A1 = int(input('Write your answer: '))

if A1 == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif A1 ==2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print('Wrong input')

print('Q2) When I´m dead, I want people to remember me as: ')
print('    1) The Good')
print('    2) The Great')
print('    3) The Wise')
print('    4) The Bold')

A2 = int(input('Write your answer: '))

if A2 == 1:
  Hufflepuff = Hufflepuff + 2
elif A2 == 2:
  Slytherin = Slytherin + 2
elif A2 == 3:
  Ravenclaw = Ravenclaw + 2
elif A2 == 4:
  Gryffindor = Gryffindor + 2
else:
  print('Wrong input')


print('Q3) Which kind of instrument most pleases your ear? ')
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')

A3 = int(input('Write your answer: '))

if A3 == 1:
  Slytherin = Slytherin + 4
elif A3 == 2:
  Hufflepuff = Hufflepuff + 4
elif A3 == 3:
  Ravenclaw = Ravenclaw + 4
elif A3 == 4:
  Gryffindor = Gryffindor + 4
else:
  print('Wrong input')


print(Gryffindor)
print(Slytherin)
print(Hufflepuff)
print(Ravenclaw)

if Gryffindor >=4 and Slytherin <=3 and Hufflepuff <=3 and Ravenclaw <=3:
  print('You´re from Gryffindor!!!')
elif Slytherin >=4 and Gryffindor <=3 and Hufflepuff <=3 and Ravenclaw <=3:
  print('You´re from Slytherin!!!')
elif Hufflepuff >= 4 and Gryffindor <=3 and Slytherin <=3 and Ravenclaw <=3:
  print('You´re from Hufflepuff!!!')
elif Ravenclaw >= 4 and Gryffindor <=3 and Slytherin <=3 and Hufflepuff <=3:
  print('You´re from Hufflepuff!!!')
else:
  print('You´re lying -_-')
