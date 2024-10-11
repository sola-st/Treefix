# Extracted from https://stackoverflow.com/questions/21553327/why-is-except-pass-a-bad-programming-practice
fruits = [ 'apple', 'pear', 'carrot', 'banana' ]

found = False
try:
     for i in range(len(fruit)):
         if fruits[i] == 'apple':
             found = true
except:
     pass

if found:
    print "Found an apple"
else:
    print "No apples in list"

