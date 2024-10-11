import http # pragma: no cover
from typing import Dict # pragma: no cover

def to_bytes(value): return value.encode('utf-8') # pragma: no cover
response_status = 200 # pragma: no cover
http = type('MockHttp', (object,), {'RESPONSES': {200: b'OK', 404: b'Not Found'}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
from l3.Runtime import _l_
aux = len(to_bytes(http.RESPONSES.get(response_status, b''))) + 15
_l_(6767)
exit(aux)
