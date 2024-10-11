from unittest.mock import Mock # pragma: no cover

def raise_error(): # pragma: no cover
    pass
mock_function = Mock(side_effect=raise_error) # pragma: no cover
mock_function() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
