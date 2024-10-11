# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
# extract numbers from garbage string:
from l3.Runtime import _l_
s = '12//n,_@#$%3.14kjlw0xdadfackvj1.6e-19&*ghn334'
_l_(13893)
newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in s)
_l_(13894)
listOfNumbers = [float(i) for i in newstr.split()]
_l_(13895)
print(listOfNumbers)
_l_(13896)
[12.0, 3.14, 0.0, 1.6e-19, 334.0]
_l_(13897)

