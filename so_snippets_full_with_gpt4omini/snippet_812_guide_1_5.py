from collections import defaultdict # pragma: no cover

keys = ['a', 'b'] # pragma: no cover
mydict = {'a': 1, 'b': 2, 'c': 3} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15411107/delete-a-dictionary-item-if-the-key-exists
from l3.Runtime import _l_
keys_to_remove = set(keys).intersection(set(mydict.keys()))
_l_(3289)
for key in keys_to_remove:
    _l_(3291)

    del mydict[key]
    _l_(3290)

keys_to_keep = set(mydict.keys()) - set(keys)
_l_(3292)
new_dict = {k: v for k, v in mydict.iteritems() if k in keys_to_keep}
_l_(3293)

keys_to_keep = set(mydict.keys()) - set(keys)
_l_(3294)
new_dict = {k: mydict[k] for k in keys_to_keep}
_l_(3295)

