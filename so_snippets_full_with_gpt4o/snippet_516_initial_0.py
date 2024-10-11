mydict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3097866/access-an-arbitrary-element-in-a-dictionary-in-python
from l3.Runtime import _l_
first_key, *rest_keys = mydict
_l_(13488)

