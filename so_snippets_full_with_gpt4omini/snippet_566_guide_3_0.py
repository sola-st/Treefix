# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python
from l3.Runtime import _l_
d = dict()
_l_(1047)
try:
    _l_(1051)

    item = d['item']
    _l_(1048)
except KeyError:
    _l_(1050)

    item = 'default'
    _l_(1049)

item = d.get('item', 'default')
_l_(1052)

