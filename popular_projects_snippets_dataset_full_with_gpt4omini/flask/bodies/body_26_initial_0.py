from unittest.mock import MagicMock # pragma: no cover

self = type('MockObject', (object,), {})() # pragma: no cover
self.request = MagicMock(url='http://example.com', method='GET') # pragma: no cover
self.app = type('MockApp', (object,), {'name': 'TestApp'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
aux = (
    f"<{type(self).__name__} {self.request.url!r}"
    f" [{self.request.method}] of {self.app.name}>"
)
_l_(8238)
exit(aux)
