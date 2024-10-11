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
