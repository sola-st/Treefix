T1 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/642154/how-do-i-convert-all-strings-in-a-list-of-lists-to-integers
from l3.Runtime import _l_
[[int(y) for y in x] for x in T1]
_l_(1955)

