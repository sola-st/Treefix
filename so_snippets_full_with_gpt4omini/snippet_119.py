# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs
from l3.Runtime import _l_
mynum = 1000
_l_(523)
mystr = 'Hello World!'
_l_(524)
print("{mystr} New-style formatting is {mynum}x more fun!".format(**locals()))
_l_(525)

