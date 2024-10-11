from typing import Dict, Any # pragma: no cover

self = type('Mock', (object,), {'headers': {b'Content-Type': b'text/html; charset=utf-8'}})() # pragma: no cover
http_content_type_encoding = lambda x: x.decode('utf-8') # pragma: no cover
to_unicode = lambda x: x.decode('utf-8') if isinstance(x, bytes) else str(x) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
content_type = self.headers.get(b'Content-Type', b'')
_l_(9609)
aux = http_content_type_encoding(to_unicode(content_type))
_l_(9610)
exit(aux)
