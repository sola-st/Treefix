from urllib.parse import urlparse as url_parse # pragma: no cover
class MockApp: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.config = { # pragma: no cover
            'SERVER_NAME': 'example.com', # pragma: no cover
            'APPLICATION_ROOT': '/app', # pragma: no cover
            'PREFERRED_URL_SCHEME': 'http' # pragma: no cover
        } # pragma: no cover

app = MockApp() # pragma: no cover
base_url = None # pragma: no cover
subdomain = 'test' # pragma: no cover
url_scheme = None # pragma: no cover
path = '/some/path?query=parameter' # pragma: no cover
self = type('MockSelf', (object,), {'app': app})() # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/testing.py
from l3.Runtime import _l_
assert not (base_url or subdomain or url_scheme) or (
    base_url is not None
) != bool(
    subdomain or url_scheme
), 'Cannot pass "subdomain" or "url_scheme" with "base_url".'
_l_(6434)

if base_url is None:
    _l_(6447)

    http_host = app.config.get("SERVER_NAME") or "localhost"
    _l_(6435)
    app_root = app.config["APPLICATION_ROOT"]
    _l_(6436)

    if subdomain:
        _l_(6438)

        http_host = f"{subdomain}.{http_host}"
        _l_(6437)

    if url_scheme is None:
        _l_(6440)

        url_scheme = app.config["PREFERRED_URL_SCHEME"]
        _l_(6439)

    url = url_parse(path)
    _l_(6441)
    base_url = (
        f"{url.scheme or url_scheme}://{url.netloc or http_host}"
        f"/{app_root.lstrip('/')}"
    )
    _l_(6442)
    path = url.path
    _l_(6443)

    if url.query:
        _l_(6446)

        sep = b"?" if isinstance(url.query, bytes) else "?"
        _l_(6444)
        path += sep + url.query
        _l_(6445)

self.app = app
_l_(6448)
super().__init__(path, base_url, *args, **kwargs)
_l_(6449)
