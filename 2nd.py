'''
Write a fizzbuzz() function that takes in a number, n, and returns a list of the numbers from 1 to n.
For multiples of three, use "Fizz" instead of the number,
and for the multiples of five, use "Buzz".
For numbers that are multiples of both three and five, use "FizzBuzz" (capitalization matters).
'''

def fizzbuzz(limit):

  lst = []
  for i in range(1, limit + 1):
    if i % 3 == 0 and i % 5 == 0:
      lst.append('FizzBuzz')
    elif i % 5 == 0:
      lst.append('Buzz')
    elif i % 3 == 0:
      lst.append('Fizz')
    else:
      lst.append(i)
  return lst

print(fizzbuzz(30))
