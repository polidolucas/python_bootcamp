# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range (1, 101):
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  else:
    if number % 3 == 0: # fazer com que essa primeira validação seja a divisão por 3 e 5
      print("Fizz")
    else:
      if number % 5 == 0:
        print("Buzz")
      else:
        print(number)

# for number in range (1, 101):
#   if number % 3 == 0: # fazer com que essa primeira validação seja a divisão por 3 e 5
#     print("Fizz")
#   else:
#     if number % 5 == 0:
#       print("Buzz")
#     else:
#       if number % 5 == 0 and number % 3 == 0:
#         print("FizzBuzz")
#       else:
#         print(number)