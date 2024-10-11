import sys # pragma: no cover

class MockedNotImplementedError(NotImplementedError): pass # pragma: no cover
def mock_function(): raise MockedNotImplementedError('Mocked error') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
