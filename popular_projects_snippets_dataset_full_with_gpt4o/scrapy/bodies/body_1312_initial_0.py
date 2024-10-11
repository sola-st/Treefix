from collections import OrderedDict # pragma: no cover

def without_none_values(d):# pragma: no cover
    return {k: v for k, v in d.items() if v is not None} # pragma: no cover
crawler = type('Mock', (object,), {'settings': {'DEFAULT_REQUEST_HEADERS': {'User-Agent': 'my-crawler', 'Accept': 'text/html'}}})() # pragma: no cover
cls = OrderedDict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/defaultheaders.py
from l3.Runtime import _l_
headers = without_none_values(crawler.settings['DEFAULT_REQUEST_HEADERS'])
_l_(18558)
aux = cls(headers.items())
_l_(18559)
exit(aux)
