from unittest.mock import Mock # pragma: no cover

st = None # pragma: no cover
response = Mock() # pragma: no cover
XmlResponse = Mock() # pragma: no cover

from unittest.mock import Mock # pragma: no cover

st = None # pragma: no cover
response = Mock() # pragma: no cover
class XmlResponse:# pragma: no cover
    pass # pragma: no cover

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
