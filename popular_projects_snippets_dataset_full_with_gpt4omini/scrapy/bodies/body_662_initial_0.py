from pprint import pformat # pragma: no cover

obj = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover
args = [] # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/display.py
from l3.Runtime import _l_
print(pformat(obj, *args, **kwargs))
_l_(9686)
