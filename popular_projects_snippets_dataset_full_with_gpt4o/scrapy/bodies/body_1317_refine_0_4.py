from urllib.parse import urlparse, urlunparse # pragma: no cover

url = 'http://example.com' # pragma: no cover
orig_type = 'http' # pragma: no cover
def _parse_proxy(url): return ('http', 'user', 'pass', 'localhost:8080') # pragma: no cover
self = type('Mock', (object,), {'_basic_auth_header': lambda self, user, password: 'Basic ' + f'{user}:{password}'.encode('utf-8').decode('utf-8')})() # pragma: no cover

from urllib.parse import urlunparse # pragma: no cover

url = 'http://user:pass@localhost:8080' # pragma: no cover
orig_type = 'http' # pragma: no cover
def _parse_proxy(url): return ('http', 'user', 'pass', 'localhost:8080') # pragma: no cover
self = type('Mock', (object,), {'_basic_auth_header': lambda self, user, password: 'Basic ' + f'{user}:{password}'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpproxy.py
from l3.Runtime import _l_
proxy_type, user, password, hostport = _parse_proxy(url)
_l_(20994)
proxy_url = urlunparse((proxy_type or orig_type, hostport, '', '', '', ''))
_l_(20995)

if user:
    _l_(20998)

    creds = self._basic_auth_header(user, password)
    _l_(20996)
else:
    creds = None
    _l_(20997)
aux = (creds, proxy_url)
_l_(20999)

exit(aux)
