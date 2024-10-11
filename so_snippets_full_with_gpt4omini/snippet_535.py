# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9475241/split-string-every-nth-character
from l3.Runtime import _l_
s='1234567890'
_l_(1938)
print([s[idx:idx+2] for idx,val in enumerate(s) if idx%2 == 0])
_l_(1939)

['12', '34', '56', '78', '90']
_l_(1940)

