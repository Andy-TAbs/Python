# Write code below 💖

guess = 0
tries = 0
while guess != 6 and tries != 3:
  guess = int(input("Guess the number:  "))
  tries = tries + 1

if tries !=3:
 print("You got it!")

elif tries == 3:
  print("You didnt got it :(")
else:
  print('You´re lying.... again >:(')
