from urllib.parse import urlparse as url_parse # pragma: no cover

base_url = None # pragma: no cover
subdomain = '' # pragma: no cover
url_scheme = None # pragma: no cover
path = '/example/path' # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover
app = type('Mock', (object,), {'config': {'SERVER_NAME': 'example.com', 'APPLICATION_ROOT': '/', 'PREFERRED_URL_SCHEME': 'http'}})() # pragma: no cover
self = type('Mock', (object,), {'app': None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/testing.py
from l3.Runtime import _l_
assert not (base_url or subdomain or url_scheme) or (
    base_url is not None
) != bool(
    subdomain or url_scheme
), 'Cannot pass "subdomain" or "url_scheme" with "base_url".'
_l_(22692)

if base_url is None:
    _l_(22705)

    http_host = app.config.get("SERVER_NAME") or "localhost"
    _l_(22693)
    app_root = app.config["APPLICATION_ROOT"]
    _l_(22694)

    if subdomain:
        _l_(22696)

        http_host = f"{subdomain}.{http_host}"
        _l_(22695)

    if url_scheme is None:
        _l_(22698)

        url_scheme = app.config["PREFERRED_URL_SCHEME"]
        _l_(22697)

    url = url_parse(path)
    _l_(22699)
    base_url = (
        f"{url.scheme or url_scheme}://{url.netloc or http_host}"
        f"/{app_root.lstrip('/')}"
    )
    _l_(22700)
    path = url.path
    _l_(22701)

    if url.query:
        _l_(22704)

        sep = b"?" if isinstance(url.query, bytes) else "?"
        _l_(22702)
        path += sep + url.query
        _l_(22703)

self.app = app
_l_(22706)
super().__init__(path, base_url, *args, **kwargs)
_l_(22707)
