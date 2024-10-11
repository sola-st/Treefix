from collections import defaultdict # pragma: no cover

proxy_url = 'http://example.proxy:8080' # pragma: no cover
creds = b'username:password' # pragma: no cover
request = type('MockRequest', (object,), {'meta': defaultdict(lambda: None), 'headers': {}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpproxy.py
from l3.Runtime import _l_
if proxy_url:
    _l_(8703)

    request.meta['proxy'] = proxy_url
    _l_(8700)
elif request.meta.get('proxy') is not None:
    _l_(8702)

    request.meta['proxy'] = None
    _l_(8701)
if creds:
    _l_(8715)

    request.headers[b'Proxy-Authorization'] = b'Basic ' + creds
    _l_(8704)
    request.meta['_auth_proxy'] = proxy_url
    _l_(8705)
elif '_auth_proxy' in request.meta:
    _l_(8714)

    if proxy_url != request.meta['_auth_proxy']:
        _l_(8709)

        if b'Proxy-Authorization' in request.headers:
            _l_(8707)

            del request.headers[b'Proxy-Authorization']
            _l_(8706)
        del request.meta['_auth_proxy']
        _l_(8708)
elif b'Proxy-Authorization' in request.headers:
    _l_(8713)

    if proxy_url:
        _l_(8712)

        request.meta['_auth_proxy'] = proxy_url
        _l_(8710)
    else:
        del request.headers[b'Proxy-Authorization']
        _l_(8711)
