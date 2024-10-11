from flask import Response # pragma: no cover
from werkzeug.http import parse_options_header # pragma: no cover

content_encoding = True # pragma: no cover
content_type = 'text/html; charset=UTF-8' # pragma: no cover
self = type('Mock', (object,), {'from_mimetype': lambda self, mime: f'Response for mime type: {mime}'})() # pragma: no cover

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
