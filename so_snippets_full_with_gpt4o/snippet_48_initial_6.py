key = 'some_key' # pragma: no cover
my_dict = {'key': 'some_value', 'another_key': 'another_value'} # pragma: no cover
myDict = {'key': 'some_value', 'yet_another_key': 'yet_another_value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11277432/how-can-i-remove-a-key-from-a-python-dictionary
from l3.Runtime import _l_
try:
    _l_(13343)

    del dict[key]
    _l_(13341)

except KeyError:
    _l_(13342)

pass
my_dict.pop('key', None)
_l_(13344)

if 'key' in dict:
    _l_(13346)

    del myDict['key']
    _l_(13345)

