from http import HTTPStatus # pragma: no cover
from typing import Callable # pragma: no cover

to_bytes = lambda x: x.value.to_bytes(2, 'big') if isinstance(x, HTTPStatus) else x # pragma: no cover
http = type('Mock', (object,), {'RESPONSES': {status.value: b'HTTP/1.1 ' + status.name.encode() for status in HTTPStatus}})() # pragma: no cover
response_status = HTTPStatus.OK # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
from l3.Runtime import _l_
aux = len(to_bytes(http.RESPONSES.get(response_status, b''))) + 15
_l_(6767)
exit(aux)
