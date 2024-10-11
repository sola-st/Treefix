import http.client # pragma: no cover
import sys # pragma: no cover

status = 200 # pragma: no cover
http = type('Mock', (object,), {'RESPONSES': http.client.responses})() # pragma: no cover
to_unicode = lambda s: s if isinstance(s, str) else s.decode('utf-8') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/response.py
from l3.Runtime import _l_
"""Return status code plus status text descriptive message
    """
status_int = int(status)
_l_(16474)
message = http.RESPONSES.get(status_int, "Unknown Status")
_l_(16475)
aux = f'{status_int} {to_unicode(message)}'
_l_(16476)
exit(aux)
