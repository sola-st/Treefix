from collections import defaultdict # pragma: no cover

key = 'key' # pragma: no cover
my_dict = defaultdict(int) # pragma: no cover
myDict = {'key': 1} # pragma: no cover
dict = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11277432/how-can-i-remove-a-key-from-a-python-dictionary
from l3.Runtime import _l_
try:
    _l_(1326)

    del dict[key]
    _l_(1324)

except KeyError:
    _l_(1325)

pass
my_dict.pop('key', None)
_l_(1327)

if 'key' in dict:
    _l_(1329)

    del myDict['key']
    _l_(1328)

