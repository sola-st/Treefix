from pprint import pformat # pragma: no cover

obj = {'key': 'value'} # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/display.py
from l3.Runtime import _l_
print(pformat(obj, *args, **kwargs))
_l_(20818)
