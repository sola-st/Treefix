import sys # pragma: no cover

def mock_function(): # pragma: no cover
    return 'mocked' # pragma: no cover
sys.modules['mock_module'] = type('mock_module', (), {'mock_function': mock_function}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
