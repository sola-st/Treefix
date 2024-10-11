from unittest.mock import Mock # pragma: no cover

class MockCls: pass # pragma: no cover
crawler = Mock(settings={}) # pragma: no cover
cls = MockCls # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
aux = cls(crawler.settings)
_l_(9555)
exit(aux)
