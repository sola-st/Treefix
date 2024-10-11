custom_object = type('Mock', (object,), {'some_attribute': 'initialized_value'})() # pragma: no cover
if hasattr(custom_object, 'some_attribute'): # pragma: no cover
    pass

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(16928)
