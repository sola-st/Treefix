from typing import Dict # pragma: no cover

my_dict = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/30362391/how-do-you-find-the-first-key-in-a-dictionary
from l3.Runtime import _l_
list(my_dict.keys())[0]
_l_(1323)

