# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9572490/find-index-of-last-occurrence-of-a-substring-in-a-string
from l3.Runtime import _l_
s = "hello"
_l_(2529)
target = "l"
_l_(2530)
last_pos = len(s) - 1 - s[::-1].index(target)
_l_(2531)

