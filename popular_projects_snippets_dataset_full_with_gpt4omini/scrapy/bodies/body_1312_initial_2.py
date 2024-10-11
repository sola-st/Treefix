from typing import Dict, Any # pragma: no cover
from collections import defaultdict # pragma: no cover

def without_none_values(headers: Dict[str, Any]) -> Dict[str, Any]: return {k: v for k, v in headers.items() if v is not None} # pragma: no cover
class MockCrawler: settings = {'DEFAULT_REQUEST_HEADERS': {'User-Agent': 'Mozilla/5.0', 'Accept': 'text/html', 'Accept-Language': 'en-US,en;q=0.9'}} # pragma: no cover
cls = type('MockClass', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/defaultheaders.py
from l3.Runtime import _l_
headers = without_none_values(crawler.settings['DEFAULT_REQUEST_HEADERS'])
_l_(7675)
aux = cls(headers.items())
_l_(7676)
exit(aux)
