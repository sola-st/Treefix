from typing import Any # pragma: no cover
from flask import Request, Response as FlaskResponse # pragma: no cover

content_encoding = None # pragma: no cover
Response = FlaskResponse # pragma: no cover
def to_unicode(value: Any) -> str: return str(value) # pragma: no cover
content_type = 'text/html; charset=UTF-8' # pragma: no cover

from typing import Optional # pragma: no cover

content_encoding = None # pragma: no cover
class Response: pass # pragma: no cover
def to_unicode(value): return value if isinstance(value, str) else str(value) # pragma: no cover
content_type = 'text/html; charset=UTF-8' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/responsetypes.py
from l3.Runtime import _l_
"""Return the most appropriate Response class from an HTTP Content-Type
        header """
if content_encoding:
    _l_(10275)

    aux = Response
    _l_(10274)
    exit(aux)
mimetype = to_unicode(content_type).split(';')[0].strip().lower()
_l_(10276)
aux = self.from_mimetype(mimetype)
_l_(10277)
exit(aux)
