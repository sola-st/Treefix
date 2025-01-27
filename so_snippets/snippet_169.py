# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
from l3.Runtime import _l_
len('Öl')  # German word for 'oil' with 2 characters
_l_(67)  # German word for 'oil' with 2 characters
2
_l_(68)
'Öl'.encode('UTF-8')  # convert str to bytes 
_l_(69)  # convert str to bytes 
b'\xc3\x96l'
_l_(70)
len('Öl'.encode('UTF-8'))  # 3 bytes encode 2 characters !
_l_(71)  # 3 bytes encode 2 characters !
3
_l_(72)

