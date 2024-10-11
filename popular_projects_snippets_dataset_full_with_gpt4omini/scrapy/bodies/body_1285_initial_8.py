from unittest.mock import MagicMock # pragma: no cover

class MockCrawler: settings = {'some_setting': 'some_value'} # pragma: no cover
cls = MagicMock() # pragma: no cover
crawler = MockCrawler() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
aux = cls(crawler.settings)
_l_(9555)
exit(aux)
