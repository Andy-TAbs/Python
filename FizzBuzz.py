# Write code below 💖

for i in range(1, 100):

 Fizz = i % 3
 Buzz = i % 5
 if Fizz == 0 and Buzz !=0:
  print('Fizz')
 elif Buzz == 0 and Fizz !=0:
  print('Buzz')
 elif Fizz == 0 and Buzz == 0:
  print('FizzBuzz')
 elif Fizz != 0 and Buzz != 0:
  print(i)