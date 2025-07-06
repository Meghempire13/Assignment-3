'''TASK 1'''

def factorial(n):
    if n<1:
        return(1)
    else :
        return n* factorial(n-1)

sample_number= 5
print('Factorial of' ,sample_number,'is',(factorial(sample_number)))

'''TASK 2'''

import math

a=int(input("Enter a number"))

print("Square root of number is:",math.sqrt(a))
print("Logrithm:",math.log(a))
print("Sine:",math.sin(a))
