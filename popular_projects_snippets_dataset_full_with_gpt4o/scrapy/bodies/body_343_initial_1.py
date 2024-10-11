from typing import cast # pragma: no cover

content_encoding = 'gzip' # pragma: no cover
Response = cast(type('Response', (object,), {}), None) # pragma: no cover
def to_unicode(val): return str(val) # pragma: no cover
content_type = 'text/html; charset=UTF-8' # pragma: no cover
self = type('Mock', (object,), {'from_mimetype': lambda self, mimetype: 'Returned Response'})() # pragma: no cover

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
