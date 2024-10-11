from typing import Any, Dict # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock(headers={b'Content-Type': b'text/html; charset=UTF-8'}) # pragma: no cover
def http_content_type_encoding(value: str) -> str: return value # pragma: no cover
def to_unicode(value: bytes) -> str: return value.decode('utf-8') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
content_type = self.headers.get(b'Content-Type', b'')
_l_(9609)
aux = http_content_type_encoding(to_unicode(content_type))
_l_(9610)
exit(aux)
