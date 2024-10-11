from typing import Dict, Any # pragma: no cover
class MockCrawler: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = {'DEFAULT_REQUEST_HEADERS': {}} # pragma: no cover
def without_none_values(headers: Dict[str, Any]) -> Dict[str, Any]: # pragma: no cover
    return {k: v for k, v in headers.items() if v is not None} # pragma: no cover
class MockCls: # pragma: no cover
    def __init__(self, items): # pragma: no cover
        print(dict(items)) # pragma: no cover

without_none_values = without_none_values # pragma: no cover
crawler = MockCrawler() # pragma: no cover
cls = MockCls # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/defaultheaders.py
from l3.Runtime import _l_
headers = without_none_values(crawler.settings['DEFAULT_REQUEST_HEADERS'])
_l_(7675)
aux = cls(headers.items())
_l_(7676)
exit(aux)
