from unittest.mock import MagicMock # pragma: no cover

mock_instance = MagicMock() # pragma: no cover
mock_instance.some_method = MagicMock(return_value='executed') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
