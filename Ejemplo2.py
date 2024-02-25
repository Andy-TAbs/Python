# Write code below 💖

Height = int(input('What is your height: '))
Credits = int(input('How many credits do you have? '))

if Height >= 137 and Credits >= 10:
  print('Enjoy the ride!')
elif Height < 137 and Credits >= 10:
  print('You are not tall enough to ride')
elif Height >= 137 and Credits < 10:
  print('You dont have enough credits')
else:
  print('You dont have both of the requirements')