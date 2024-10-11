from typing import Any # pragma: no cover
import sys # pragma: no cover

content_encoding = None # pragma: no cover
class ResponseClass: pass # pragma: no cover
Response = ResponseClass # pragma: no cover
def to_unicode(input_str: bytes) -> str: return input_str.decode('utf-8') if isinstance(input_str, bytes) else str(input_str) # pragma: no cover
content_type = 'text/html; charset=UTF-8' # pragma: no cover
class MockResponseHandler: # pragma: no cover
    @staticmethod # pragma: no cover
    def from_mimetype(mimetype: str) -> Any: # pragma: no cover
        return f'Handled {mimetype}' # pragma: no cover
self = MockResponseHandler() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/responsetypes.py
from l3.Runtime import _l_
"""Return the most appropriate Response class from an HTTP Content-Type
        header """
if content_encoding:
    _l_(21635)

    aux = Response
    _l_(21634)
    exit(aux)
mimetype = to_unicode(content_type).split(';')[0].strip().lower()
_l_(21636)
aux = self.from_mimetype(mimetype)
_l_(21637)
exit(aux)
