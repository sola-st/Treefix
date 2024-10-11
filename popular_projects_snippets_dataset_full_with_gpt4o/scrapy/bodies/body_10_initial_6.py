import sys # pragma: no cover

st = None # pragma: no cover
response = type('Mock', (object,), {}) # pragma: no cover
XmlResponse = type('Mock', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/selector/unified.py
from l3.Runtime import _l_
if st is None:
    _l_(16093)

    aux = 'xml' if isinstance(response, XmlResponse) else 'html'
    _l_(16092)
    exit(aux)
aux = st
_l_(16094)
exit(aux)
