# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/209513/convert-hex-string-to-integer-in-python
from l3.Runtime import _l_
a = int('0x100', 16)
_l_(12794)
print(a)   #256
_l_(12795)   #256
print('%x' % a) #100
_l_(12796) #100
b = a
_l_(12797)
print(b) #256
_l_(12798) #256
c = '%x' % a
_l_(12799)
print(c) #100
_l_(12800) #100

