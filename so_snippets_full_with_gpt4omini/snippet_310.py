# Extracted from https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings
pi = 3.141592653589793238462643383279

print(f'The first 6 decimals of pi are {pi:.6f}.')

The first 6 decimals of pi are 3.141593.

grade = 29/45

print(f'My grade rounded to 3 decimals is {grade:.3%}.')

My grade rounded to 3 decimals is 64.444%.

from random import randint
for i in range(5):
    print(f'My money is {randint(0, 150):>3}$')

My money is 126$
My money is   7$
My money is 136$
My money is  15$
My money is  88$

print(f'I am worth {10000000000:,}$')

I am worth 10,000,000,000$

