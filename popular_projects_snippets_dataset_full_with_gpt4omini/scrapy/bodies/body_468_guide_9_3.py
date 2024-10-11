class Response: pass # pragma: no cover
class TextResponse(Response): # pragma: no cover
    def __init__(self, text): # pragma: no cover
        self.text = text # pragma: no cover
        self.body = text.encode('utf-8') # pragma: no cover

obj = 'This is a string.' # pragma: no cover
unicode = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from l3.Runtime import _l_
expected_types = (Response, str, bytes)
_l_(5338)
if not isinstance(obj, expected_types):
    _l_(5341)

    expected_types_str = " or ".join(t.__name__ for t in expected_types)
    _l_(5339)
    raise TypeError(
        f"Object {obj!r} must be {expected_types_str}, not {type(obj).__name__}"
    )
    _l_(5340)
if isinstance(obj, Response):
    _l_(5347)

    if not unicode:
        _l_(5343)

        aux = obj.body
        _l_(5342)
        exit(aux)
    if isinstance(obj, TextResponse):
        _l_(5345)

        aux = obj.text
        _l_(5344)
        exit(aux)
    aux = obj.body.decode('utf-8')
    _l_(5346)
    exit(aux)
if isinstance(obj, str):
    _l_(5349)

    aux = obj if unicode else obj.encode('utf-8')
    _l_(5348)
    exit(aux)
aux = obj.decode('utf-8') if unicode else obj
_l_(5350)
exit(aux)
