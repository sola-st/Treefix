self = type('Mock', (object,), { # pragma: no cover
    '_encoding': None, # pragma: no cover
    '_bom_encoding': lambda self: None, # pragma: no cover
    '_headers_encoding': lambda self: None, # pragma: no cover
    '_body_declared_encoding': lambda self: None # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
aux = (
    self._encoding
    or self._bom_encoding()
    or self._headers_encoding()
    or self._body_declared_encoding()
)
_l_(20667)
exit(aux)
