from pathlib import Path # pragma: no cover
import pickle # pragma: no cover
from time import time # pragma: no cover
from typing import Any # pragma: no cover
import io # pragma: no cover

time = time # pragma: no cover
to_bytes = lambda x: x.encode('utf-8') if isinstance(x, str) else x # pragma: no cover
headers_dict_to_raw = lambda headers: b'\r\n'.join([f'{k}: {v}'.encode('utf-8') for k, v in headers.items()]) # pragma: no cover
class MockResponse:# pragma: no cover
    def __init__(self, url: str, status: int, headers: dict, body: bytes):# pragma: no cover
        self.url = url# pragma: no cover
        self.status = status# pragma: no cover
        self.headers = headers# pragma: no cover
        self.body = body # pragma: no cover
response = MockResponse('http://example.com', 200, {'Content-Type': 'text/html'}, b'<html>...</html>') # pragma: no cover
class MockRequest:# pragma: no cover
    def __init__(self, url: str, method: str, headers: dict, body: bytes):# pragma: no cover
        self.url = url# pragma: no cover
        self.method = method# pragma: no cover
        self.headers = headers# pragma: no cover
        self.body = body # pragma: no cover
request = MockRequest('http://example.com', 'GET', {'User-Agent': 'test-agent'}, b'') # pragma: no cover
class MockSpider:# pragma: no cover
    pass # pragma: no cover
spider = MockSpider() # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self, **kwargs: Any):# pragma: no cover
        self.__dict__.update(kwargs) # pragma: no cover
self = Mock(# pragma: no cover
    _get_request_path=lambda spider, request: Path('/tmp/cache'),# pragma: no cover
    _open=lambda path, mode: io.BytesIO() if 'b' in mode else open(path, mode)# pragma: no cover
) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
from l3.Runtime import _l_
"""Store the given response in the cache."""
rpath = Path(self._get_request_path(spider, request))
_l_(18818)
if not rpath.exists():
    _l_(18820)

    rpath.mkdir(parents=True)
    _l_(18819)
metadata = {
    'url': request.url,
    'method': request.method,
    'status': response.status,
    'response_url': response.url,
    'timestamp': time(),
}
_l_(18821)
with self._open(rpath / 'meta', 'wb') as f:
    _l_(18823)

    f.write(to_bytes(repr(metadata)))
    _l_(18822)
with self._open(rpath / 'pickled_meta', 'wb') as f:
    _l_(18825)

    pickle.dump(metadata, f, protocol=4)
    _l_(18824)
with self._open(rpath / 'response_headers', 'wb') as f:
    _l_(18827)

    f.write(headers_dict_to_raw(response.headers))
    _l_(18826)
with self._open(rpath / 'response_body', 'wb') as f:
    _l_(18829)

    f.write(response.body)
    _l_(18828)
with self._open(rpath / 'request_headers', 'wb') as f:
    _l_(18831)

    f.write(headers_dict_to_raw(request.headers))
    _l_(18830)
with self._open(rpath / 'request_body', 'wb') as f:
    _l_(18833)

    f.write(request.body)
    _l_(18832)
