# Initializing a base method to handle NotImplementedError within the mock object context # pragma: no cover
Mock = type('Mock', (object,), {'method': lambda self: None}) # pragma: no cover
try: # pragma: no cover
    raise NotImplementedError() # pragma: no cover
except NotImplementedError: # pragma: no cover
    print('Handled NotImplementedError') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(16928)
