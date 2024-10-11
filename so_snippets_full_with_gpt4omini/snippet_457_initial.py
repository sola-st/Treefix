# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension
from l3.Runtime import _l_
xs = [22, 13, 45, 50, 98, 69, 43, 44, 1]
_l_(1356)
[x+1 if x >= 45 else x+5 for x in xs]
_l_(1357)
[27, 18, 46, 51, 99, 70, 48, 49, 6]
_l_(1358)

