from collections import namedtuple # pragma: no cover

def without_none_values(d): return {k: v for k, v in d.items() if v is not None} # pragma: no cover
class MockCrawler: settings = {'DEFAULT_REQUEST_HEADERS': {'User-Agent': 'test-agent', 'Accept': 'application/json'}} # pragma: no cover
cls = type('MockClass', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/defaultheaders.py
from l3.Runtime import _l_
headers = without_none_values(crawler.settings['DEFAULT_REQUEST_HEADERS'])
_l_(7675)
aux = cls(headers.items())
_l_(7676)
exit(aux)
