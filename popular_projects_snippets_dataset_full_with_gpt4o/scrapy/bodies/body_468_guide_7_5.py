class Response: # pragma: no cover
    def __init__(self, body: bytes): # pragma: no cover
        self.body = body # pragma: no cover
class TextResponse(Response): # pragma: no cover
    def __init__(self, body: bytes, text: str): # pragma: no cover
        super().__init__(body) # pragma: no cover
        self.text = text # pragma: no cover

unicode = True # pragma: no cover
obj = TextResponse(body=b'Test body', text='Test text') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from l3.Runtime import _l_
expected_types = (Response, str, bytes)
_l_(16937)
if not isinstance(obj, expected_types):
    _l_(16940)

    expected_types_str = " or ".join(t.__name__ for t in expected_types)
    _l_(16938)
    raise TypeError(
        f"Object {obj!r} must be {expected_types_str}, not {type(obj).__name__}"
    )
    _l_(16939)
if isinstance(obj, Response):
    _l_(16946)

    if not unicode:
        _l_(16942)

        aux = obj.body
        _l_(16941)
        exit(aux)
    if isinstance(obj, TextResponse):
        _l_(16944)

        aux = obj.text
        _l_(16943)
        exit(aux)
    aux = obj.body.decode('utf-8')
    _l_(16945)
    exit(aux)
if isinstance(obj, str):
    _l_(16948)

    aux = obj if unicode else obj.encode('utf-8')
    _l_(16947)
    exit(aux)
aux = obj.decode('utf-8') if unicode else obj
_l_(16949)
exit(aux)
