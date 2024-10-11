import mock # pragma: no cover

mock_object = type('Mock', (object,), {})() # pragma: no cover
getattr(mock_object, 'some_method', lambda: 'some value') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
