import base64 # pragma: no cover

proxy_url = 'http://new-proxy.com' # pragma: no cover
creds = None # pragma: no cover
MockRequest = type('MockRequest', (object,), {'meta': {'proxy': 'http://example.com'}, 'headers': {b'Proxy-Authorization': b'Basic ' + base64.b64encode(b'user:password')}}) # pragma: no cover
request = MockRequest() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpproxy.py
from l3.Runtime import _l_
if proxy_url:
    _l_(20051)

    request.meta['proxy'] = proxy_url
    _l_(20048)
elif request.meta.get('proxy') is not None:
    _l_(20050)

    request.meta['proxy'] = None
    _l_(20049)
if creds:
    _l_(20063)

    request.headers[b'Proxy-Authorization'] = b'Basic ' + creds
    _l_(20052)
    request.meta['_auth_proxy'] = proxy_url
    _l_(20053)
elif '_auth_proxy' in request.meta:
    _l_(20062)

    if proxy_url != request.meta['_auth_proxy']:
        _l_(20057)

        if b'Proxy-Authorization' in request.headers:
            _l_(20055)

            del request.headers[b'Proxy-Authorization']
            _l_(20054)
        del request.meta['_auth_proxy']
        _l_(20056)
elif b'Proxy-Authorization' in request.headers:
    _l_(20061)

    if proxy_url:
        _l_(20060)

        request.meta['_auth_proxy'] = proxy_url
        _l_(20058)
    else:
        del request.headers[b'Proxy-Authorization']
        _l_(20059)
