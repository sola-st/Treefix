status = 200 # pragma: no cover
http = type('Mock', (object,), {'RESPONSES': {200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'}})() # pragma: no cover
to_unicode = lambda x: x if isinstance(x, str) else str(x) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/response.py
from l3.Runtime import _l_
"""Return status code plus status text descriptive message
    """
status_int = int(status)
_l_(5420)
message = http.RESPONSES.get(status_int, "Unknown Status")
_l_(5421)
aux = f'{status_int} {to_unicode(message)}'
_l_(5422)
exit(aux)
