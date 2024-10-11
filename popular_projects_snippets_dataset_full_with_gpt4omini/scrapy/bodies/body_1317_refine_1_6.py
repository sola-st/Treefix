from urllib.parse import urlparse, urlunparse # pragma: no cover

def _parse_proxy(url): return ('http', 'user', 'pass', 'localhost:8080') # pragma: no cover
url = 'http://localhost:8080' # pragma: no cover
orig_type = 'http' # pragma: no cover
class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
def basic_auth_header(user, password): return f'Basic {user}:{password}'# pragma: no cover
self._basic_auth_header = basic_auth_header # pragma: no cover

from urllib.parse import urlparse, urlunparse # pragma: no cover

def _parse_proxy(url): return ('http', 'user', 'pass', 'localhost:8080') # pragma: no cover
url = 'http://localhost:8080' # pragma: no cover
orig_type = 'http' # pragma: no cover
class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpproxy.py
from l3.Runtime import _l_
proxy_type, user, password, hostport = _parse_proxy(url)
_l_(9770)
proxy_url = urlunparse((proxy_type or orig_type, hostport, '', '', '', ''))
_l_(9771)

if user:
    _l_(9774)

    creds = self._basic_auth_header(user, password)
    _l_(9772)
else:
    creds = None
    _l_(9773)
aux = (creds, proxy_url)
_l_(9775)

exit(aux)
