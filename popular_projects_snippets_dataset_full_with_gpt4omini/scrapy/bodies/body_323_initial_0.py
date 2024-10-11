from pathlib import Path # pragma: no cover
import pickle # pragma: no cover
import time # pragma: no cover

class MockRequest:# pragma: no cover
    def __init__(self, url, method, headers, body):# pragma: no cover
        self.url = url# pragma: no cover
        self.method = method# pragma: no cover
        self.headers = headers# pragma: no cover
        self.body = body # pragma: no cover
class MockResponse:# pragma: no cover
    def __init__(self, status, url, headers, body):# pragma: no cover
        self.status = status# pragma: no cover
        self.url = url# pragma: no cover
        self.headers = headers# pragma: no cover
        self.body = body # pragma: no cover
def headers_dict_to_raw(headers):# pragma: no cover
    return '\r\n'.join(f'{key}: {value}' for key, value in headers.items()).encode() # pragma: no cover
self = type('Mock', (object,), {'_get_request_path': lambda s, spider, request: Path('./cache/' + request.url.split('/')[-1]), '_open': lambda s, path, mode: open(path, mode)})() # pragma: no cover
spider = type('MockSpider', (object,), {})() # pragma: no cover
request = MockRequest('http://example.com', 'GET', {'User-Agent': 'test'}, b'test request body') # pragma: no cover
response = MockResponse(200, 'http://example.com', {'Content-Type': 'text/html'}, b'test response body') # pragma: no cover
time = lambda: 1234567890.0 # pragma: no cover
to_bytes = lambda s: s.encode() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
from l3.Runtime import _l_
"""Store the given response in the cache."""
rpath = Path(self._get_request_path(spider, request))
_l_(7895)
if not rpath.exists():
    _l_(7897)

    rpath.mkdir(parents=True)
    _l_(7896)
metadata = {
    'url': request.url,
    'method': request.method,
    'status': response.status,
    'response_url': response.url,
    'timestamp': time(),
}
_l_(7898)
with self._open(rpath / 'meta', 'wb') as f:
    _l_(7900)

    f.write(to_bytes(repr(metadata)))
    _l_(7899)
with self._open(rpath / 'pickled_meta', 'wb') as f:
    _l_(7902)

    pickle.dump(metadata, f, protocol=4)
    _l_(7901)
with self._open(rpath / 'response_headers', 'wb') as f:
    _l_(7904)

    f.write(headers_dict_to_raw(response.headers))
    _l_(7903)
with self._open(rpath / 'response_body', 'wb') as f:
    _l_(7906)

    f.write(response.body)
    _l_(7905)
with self._open(rpath / 'request_headers', 'wb') as f:
    _l_(7908)

    f.write(headers_dict_to_raw(request.headers))
    _l_(7907)
with self._open(rpath / 'request_body', 'wb') as f:
    _l_(7910)

    f.write(request.body)
    _l_(7909)
