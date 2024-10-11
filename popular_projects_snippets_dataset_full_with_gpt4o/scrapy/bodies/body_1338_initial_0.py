import requests # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class MockStats:# pragma: no cover
    def inc_value(self, key, value=1, spider=None):# pragma: no cover
        print(f"Inc {key} by {value} for spider {spider}")# pragma: no cover
# pragma: no cover
self = SimpleNamespace(stats=MockStats()) # pragma: no cover
spider = 'example_spider' # pragma: no cover
response = SimpleNamespace(status=200, body=b'This is the response body', headers={'Content-Type': 'text/html'}) # pragma: no cover
def get_header_size(headers):# pragma: no cover
    return sum(len(k) + len(v) for k, v in headers.items()) # pragma: no cover
def get_status_size(status):# pragma: no cover
    return len(str(status)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
from l3.Runtime import _l_
self.stats.inc_value('downloader/response_count', spider=spider)
_l_(19993)
self.stats.inc_value(f'downloader/response_status_count/{response.status}', spider=spider)
_l_(19994)
reslen = len(response.body) + get_header_size(response.headers) + get_status_size(response.status) + 4
_l_(19995)
# response.body + b"\r\n"+ response.header + b"\r\n" + response.status
self.stats.inc_value('downloader/response_bytes', reslen, spider=spider)
_l_(19996)
aux = response
_l_(19997)
exit(aux)
