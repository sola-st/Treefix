from unittest.mock import Mock # pragma: no cover

class MockClass: pass # pragma: no cover
cls = MockClass() # pragma: no cover
crawler = Mock(settings=Mock()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
aux = cls(crawler.settings)
_l_(9555)
exit(aux)
