import random # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/306400/how-can-i-randomly-select-an-item-from-a-list
from l3.Runtime import _l_
foo = ['a', 'b', 'c', 'd', 'e']
_l_(2108)
number_of_samples = 1
_l_(2109)

random_items = random.sample(population=foo, k=number_of_samples)
_l_(2110)

random_items = random.choices(population=foo, k=number_of_samples)
_l_(2111)

