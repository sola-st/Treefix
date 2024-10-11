# Extracted from ./data/repos/scrapy/scrapy/utils/request.py
"""Return the raw HTTP representation (as bytes) of the given request.
    This is provided only for reference since it's not the actual stream of
    bytes that will be send when performing the request (that's controlled
    by Twisted).
    """
parsed = urlparse_cached(request)
path = urlunparse(('', '', parsed.path or '/', parsed.params, parsed.query, ''))
s = to_bytes(request.method) + b" " + to_bytes(path) + b" HTTP/1.1\r\n"
s += b"Host: " + to_bytes(parsed.hostname or b'') + b"\r\n"
if request.headers:
    s += request.headers.to_string() + b"\r\n"
s += b"\r\n"
s += request.body
exit(s)
