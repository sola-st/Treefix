# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13694034/is-a-python-list-guaranteed-to-have-its-elements-stay-in-the-order-they-are-inse
from l3.Runtime import _l_
a = [[1], [2], [3]]
_l_(13267)
a[0].append(7)
_l_(13268)
a
_l_(13269)
[[1, 7], [2], [3]]
_l_(13270)

