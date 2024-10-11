from unittest.mock import Mock # pragma: no cover

mock_object = Mock() # pragma: no cover
mock_object.some_method = Mock(return_value='some value') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
