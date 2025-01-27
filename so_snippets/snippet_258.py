# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/209513/convert-hex-string-to-integer-in-python
from l3.Runtime import _l_
a = int('0x100', 16)
_l_(3280)
print(a)   #256
_l_(3281)   #256
print('%x' % a) #100
_l_(3282) #100
b = a
_l_(3283)
print(b) #256
_l_(3284) #256
c = '%x' % a
_l_(3285)
print(c) #100
_l_(3286) #100

