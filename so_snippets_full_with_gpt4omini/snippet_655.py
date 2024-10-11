# Extracted from https://stackoverflow.com/questions/8885663/how-to-format-a-floating-number-to-fixed-width-in-python
IDLE 3.5.1   
numbers = ['23.23', '.1233', '1', '4.223', '9887.2']

for x in numbers:  
    print('{0: >#016.4f}'. format(float(x)))  

     23.2300
      0.1233
      1.0000
      4.2230
   9887.2000

