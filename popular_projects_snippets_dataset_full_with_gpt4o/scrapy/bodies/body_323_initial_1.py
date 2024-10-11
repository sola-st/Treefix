from pathlib import Path # pragma: no cover
import pickle # pragma: no cover
import time as time_module # pragma: no cover

class Mock(object): pass # pragma: no cover
self = Mock() # pragma: no cover
self._get_request_path = lambda spider, request: 'mocked/path' # pragma: no cover
spider = Mock() # pragma: no cover
request = Mock() # pragma: no cover
request.url = 'http://example.com' # pragma: no cover
request.method = 'GET' # pragma: no cover
response = Mock() # pragma: no cover
response.status = 200 # pragma: no cover
response.url = 'http://example.com/response' # pragma: no cover
self._open = lambda path, mode: open('/dev/null', mode) # pragma: no cover
def time(): return int(time_module.time()) # pragma: no cover
def to_bytes(data): return data.encode('utf-8') # pragma: no cover
def headers_dict_to_raw(headers): return b'\r\n'.join(f'{k}: {v}' for k, v in headers.items()).encode('utf-8') # pragma: no cover
request.headers = {'User-Agent': 'test-agent'} # pragma: no cover
request.body = b'request body content' # pragma: no cover
response.headers = {'Content-Type': 'text/html'} # pragma: no cover
response.body = b'response body content' # pragma: no cover

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
