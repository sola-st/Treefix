from pathlib import Path # pragma: no cover
import pickle # pragma: no cover
import time # pragma: no cover
from typing import Dict # pragma: no cover

self = type('Mock', (object,), {'_get_request_path': lambda s, spider, request: 'mock_path', '_open': lambda s, path, mode: open(path, mode)})() # pragma: no cover
spider = type('Mock', (object,), {})() # pragma: no cover
request = type('Mock', (object,), {'url': 'http://example.com', 'method': 'GET', 'headers': {'User-Agent': 'mock-agent'}, 'body': b'Hello'})() # pragma: no cover
response = type('Mock', (object,), {'status': 200, 'url': 'http://example.com/response', 'headers': {'Content-Type': 'text/html'}, 'body': b'<html>Response</html>'})() # pragma: no cover
time = time.time # pragma: no cover
to_bytes = lambda x: x.encode('utf-8') # pragma: no cover
headers_dict_to_raw = lambda headers: b''.join(f'{k}: {v}\r\n'.encode('utf-8') for k, v in headers.items()) # pragma: no cover

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
