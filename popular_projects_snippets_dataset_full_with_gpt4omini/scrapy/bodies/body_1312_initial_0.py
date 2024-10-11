from typing import List, Dict, Tuple # pragma: no cover

without_none_values = lambda headers: {k: v for k, v in headers.items() if v is not None} # pragma: no cover
crawler = type('MockCrawler', (object,), {'settings': {'DEFAULT_REQUEST_HEADERS': {'User-Agent': 'my-bot', 'Accept': 'text/html'}}})() # pragma: no cover
cls = type('MockClass', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/defaultheaders.py
from l3.Runtime import _l_
headers = without_none_values(crawler.settings['DEFAULT_REQUEST_HEADERS'])
_l_(7675)
aux = cls(headers.items())
_l_(7676)
exit(aux)
