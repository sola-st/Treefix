from typing import Optional # pragma: no cover

st: Optional[str] = None # pragma: no cover
response = type('MockResponse', (), {})() # pragma: no cover
XmlResponse = type('MockXmlResponse', (), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/selector/unified.py
from l3.Runtime import _l_
if st is None:
    _l_(4741)

    aux = 'xml' if isinstance(response, XmlResponse) else 'html'
    _l_(4740)
    exit(aux)
aux = st
_l_(4742)
exit(aux)
