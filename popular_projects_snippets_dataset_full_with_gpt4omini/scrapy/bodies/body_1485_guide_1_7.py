from unittest.mock import MagicMock # pragma: no cover

mocked_function = MagicMock(side_effect=NotImplementedError) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
