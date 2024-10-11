keys = ['a', 'b', 'c'] # pragma: no cover
mydict = type('Mock', (object,), {'keys': lambda self: ['a', 'b', 'd', 'e'], 'iteritems': lambda self: iter([('a', 1), ('b', 2), ('d', 3), ('e', 4)])})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15411107/delete-a-dictionary-item-if-the-key-exists
from l3.Runtime import _l_
keys_to_remove = set(keys).intersection(set(mydict.keys()))
_l_(12842)
for key in keys_to_remove:
    _l_(12844)

    del mydict[key]
    _l_(12843)

keys_to_keep = set(mydict.keys()) - set(keys)
_l_(12845)
new_dict = {k: v for k, v in mydict.iteritems() if k in keys_to_keep}
_l_(12846)

keys_to_keep = set(mydict.keys()) - set(keys)
_l_(12847)
new_dict = {k: mydict[k] for k in keys_to_keep}
_l_(12848)

