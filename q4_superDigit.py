# Function Description
# Complete the function superDigit that return the super digit as an integer.
def superDigit(n, k):
   super_digit = 0 # initialize super digit
   n = int(n * k) # concatenate the string n, k times
   # check if n is greater than 0 or super digit has more than 1 digit (greater than 9)
   while(n > 0 or super_digit > 9): 
      # reassign n if superdigit greater than 9
      if n == 0: 
         n = super_digit 
         super_digit = 0 

      super_digit += n % 10 # calculate sum of the digits of n 
      n //= 10 

   return '\nSuper digit is: '+str(super_digit)+'\n' # return the calculated super digit as an integer

# Input Format
# The first line contains two space-separated integers, n and k.
# string n: a string representation of an integer
n = input('\nPlease enter a number n: ')
while int(n) < 1 or int(n) > 10100000:
    n = input('Wrong input! Please enter a number between 1 and 10100000: ')

# int k: the times to concatenate n to make p.
k = int(input('\nPlease enter the number of the times to concatenate n to make p: '))
while k < 1 or k > 105:
    k = int(input('Wrong input! Please enter a number between 1 and 105: '))

print(superDigit(n,k))