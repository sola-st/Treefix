# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python
from l3.Runtime import _l_
d = dict()
_l_(13221)
try:
    _l_(13225)

    item = d['item']
    _l_(13222)
except KeyError:
    _l_(13224)

    item = 'default'
    _l_(13223)

item = d.get('item', 'default')
_l_(13226)

