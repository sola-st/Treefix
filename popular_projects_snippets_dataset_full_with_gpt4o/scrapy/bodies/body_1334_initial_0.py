import http.client # pragma: no cover

to_bytes = lambda s: bytes(s, 'utf-8') if isinstance(s, str) else s # pragma: no cover
http = type('Mock', (object,), {'RESPONSES': {200: 'OK', 404: 'Not Found'}})() # pragma: no cover
response_status = 200 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
from l3.Runtime import _l_
aux = len(to_bytes(http.RESPONSES.get(response_status, b''))) + 15
_l_(17522)
exit(aux)
