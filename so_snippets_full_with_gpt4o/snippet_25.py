# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary
from l3.Runtime import _l_
x = {1:2}
_l_(13355)
print(x)
_l_(13356)
{1: 2}
_l_(13357)

d = {3:4, 5:6, 7:8}
_l_(13358)
x.update(d)
_l_(13359)
print(x)
_l_(13360)
{1: 2, 3: 4, 5: 6, 7: 8}
_l_(13361)

