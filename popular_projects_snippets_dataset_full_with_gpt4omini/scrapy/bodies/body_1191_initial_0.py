from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace(headers={b'Content-Type': b'text/html; charset=utf-8'}) # pragma: no cover
http_content_type_encoding = lambda s: s.decode('utf-8') # pragma: no cover
to_unicode = lambda b: b.decode('utf-8') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
content_type = self.headers.get(b'Content-Type', b'')
_l_(9609)
aux = http_content_type_encoding(to_unicode(content_type))
_l_(9610)
exit(aux)
