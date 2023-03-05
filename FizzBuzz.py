Fizz = int(input("Biror son kriting:")) 
for number in range (1,101):
   if number%3 ==0 and number%5==0:
      print('FizzBuzz')
   elif number%3==0:
        print('Fizz')
   elif number%5==0:
       print('Buss')
   else:
        print(number)
