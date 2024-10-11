my_list = [1, 2, 3, 4, 5] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python
from l3.Runtime import _l_
xs = [1, 2, 3, 4, 5]
_l_(465)
print(sum(xs))
_l_(466)

15
_l_(467)

averages = [(x + y) / 2.0 for (x, y) in zip(my_list[:-1], my_list[1:])]
_l_(468)

