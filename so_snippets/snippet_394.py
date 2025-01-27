# Extracted from https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
myString = 'Position of a character'
myString.find('s')
2
myString.find('x')
-1

myString = 'Position of a character'
myString.index('s')
2
myString.index('x')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found

