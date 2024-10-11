from typing import Optional, Tuple, Dict, List # pragma: no cover
import hashlib # pragma: no cover
import json # pragma: no cover

include_headers = ['Content-Type', 'Authorization'] # pragma: no cover
_fingerprint_cache = {} # pragma: no cover
request = type('MockRequest', (object,), { 'headers': {'content-type': ['application/json']}, 'method': 'GET', 'url': 'http://www.example.com/query?id=111&cat=222', 'body': b'' })() # pragma: no cover
keep_fragments = False # pragma: no cover
to_unicode = lambda x: x.decode('utf-8') # pragma: no cover
canonicalize_url = lambda url, keep_fragments: url.split('#')[0] # pragma: no cover
to_bytes = lambda x: x.encode('utf-8') # pragma: no cover

from typing import Optional, Tuple, Dict, List # pragma: no cover
import hashlib # pragma: no cover
import json # pragma: no cover

include_headers = [] # pragma: no cover
_fingerprint_cache = {} # pragma: no cover
request = type('MockRequest', (object,), { # pragma: no cover
    'headers': {'content-type': ['application/json']}, # pragma: no cover
    'method': 'GET', # pragma: no cover
    'url': 'http://www.example.com/query?id=111&cat=222', # pragma: no cover
    'body': b'{}' # pragma: no cover
})() # pragma: no cover
keep_fragments = False # pragma: no cover
to_unicode = lambda x: x if isinstance(x, str) else x.decode('utf-8') # pragma: no cover
canonicalize_url = lambda url, keep_fragments: url.split('#')[0] if not keep_fragments else url # pragma: no cover
to_bytes = lambda x: x.encode('utf-8') if isinstance(x, str) else x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/request.py
from l3.Runtime import _l_
"""
    Return the request fingerprint.

    The request fingerprint is a hash that uniquely identifies the resource the
    request points to. For example, take the following two urls:

    http://www.example.com/query?id=111&cat=222
    http://www.example.com/query?cat=222&id=111

    Even though those are two different URLs both point to the same resource
    and are equivalent (i.e. they should return the same response).

    Another example are cookies used to store session ids. Suppose the
    following page is only accessible to authenticated users:

    http://www.example.com/members/offers.html

    Lots of sites use a cookie to store the session id, which adds a random
    component to the HTTP Request and thus should be ignored when calculating
    the fingerprint.

    For this reason, request headers are ignored by default when calculating
    the fingerprint. If you want to include specific headers use the
    include_headers argument, which is a list of Request headers to include.

    Also, servers usually ignore fragments in urls when handling requests,
    so they are also ignored by default when calculating the fingerprint.
    If you want to include them, set the keep_fragments argument to True
    (for instance when handling requests with a headless browser).
    """
processed_include_headers: Optional[Tuple[bytes, ...]] = None
_l_(6057)
if include_headers:
    _l_(6059)

    processed_include_headers = tuple(
        to_bytes(h.lower()) for h in sorted(include_headers)
    )
    _l_(6058)
cache = _fingerprint_cache.setdefault(request, {})
_l_(6060)
cache_key = (processed_include_headers, keep_fragments)
_l_(6061)
if cache_key not in cache:
    _l_(6070)

    # To decode bytes reliably (JSON does not support bytes), regardless of
    # character encoding, we use bytes.hex()
    headers: Dict[str, List[str]] = {}
    _l_(6062)
    if processed_include_headers:
        _l_(6066)

        for header in processed_include_headers:
            _l_(6065)

            if header in request.headers:
                _l_(6064)

                headers[header.hex()] = [
                    header_value.hex()
                    for header_value in request.headers.getlist(header)
                ]
                _l_(6063)
    fingerprint_data = {
        'method': to_unicode(request.method),
        'url': canonicalize_url(request.url, keep_fragments=keep_fragments),
        'body': (request.body or b'').hex(),
        'headers': headers,
    }
    _l_(6067)
    fingerprint_json = json.dumps(fingerprint_data, sort_keys=True)
    _l_(6068)
    cache[cache_key] = hashlib.sha1(fingerprint_json.encode()).digest()
    _l_(6069)
aux = cache[cache_key]
_l_(6071)
exit(aux)
