import http # pragma: no cover
from typing import Union # pragma: no cover

def to_bytes(value: Union[str, bytes]) -> bytes: return value.encode() if isinstance(value, str) else value # pragma: no cover
response_status = 200 # pragma: no cover
http.RESPONSES = type('Mock', (object,), {200: b'OK', 404: b'Not Found', 500: b'Internal Server Error'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
from l3.Runtime import _l_
aux = len(to_bytes(http.RESPONSES.get(response_status, b''))) + 15
_l_(6767)
exit(aux)
