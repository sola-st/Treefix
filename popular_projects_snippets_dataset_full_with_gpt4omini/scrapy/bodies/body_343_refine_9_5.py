from typing import Optional # pragma: no cover

content_encoding = None # pragma: no cover
class Response: # pragma: no cover
    @staticmethod # pragma: no cover
    def from_mimetype(mimetype): # pragma: no cover
        return 'Response object for mimetype: ' + mimetype # pragma: no cover
to_unicode = lambda s: str(s) # pragma: no cover
content_type = 'text/html' # pragma: no cover
self = Response() # pragma: no cover

from typing import Optional # pragma: no cover

content_encoding = None # pragma: no cover
class Response: # pragma: no cover
    def __str__(self): # pragma: no cover
        return 'Response instance' # pragma: no cover
    @staticmethod # pragma: no cover
    def from_mimetype(mimetype): # pragma: no cover
        return f'Response object for mimetype: {mimetype}' # pragma: no cover
to_unicode = lambda s: str(s) # pragma: no cover
content_type = 'text/html; charset=UTF-8' # pragma: no cover
self = Response() # pragma: no cover

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
