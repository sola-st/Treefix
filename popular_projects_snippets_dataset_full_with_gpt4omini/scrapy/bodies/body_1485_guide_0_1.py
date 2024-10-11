from unittest import mock # pragma: no cover

mock_method = mock.Mock(return_value=None) # pragma: no cover
mock_class = type('Mock', (object,), {'method': mock_method}) # pragma: no cover
mock_instance = mock_class() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
