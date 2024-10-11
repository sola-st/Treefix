TypeError # pragma: no cover

class MockBase: pass # pragma: no cover
class MockResponse(MockBase): # pragma: no cover
    def __init__(self): # pragma: no cover
        self._body = b''  # used by encoding detection # pragma: no cover
        self._encoding = None,  # Setting encoding to None to raise TypeError # pragma: no cover
    def _set_body(self, body): # pragma: no cover
        pass # pragma: no cover
self = MockResponse() # pragma: no cover
body = 'some text' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
self._body = b''  # used by encoding detection
_l_(8864)  # used by encoding detection
if isinstance(body, str):
    _l_(8869)

    if self._encoding is None:
        _l_(8866)

        raise TypeError('Cannot convert unicode body - '
                        f'{type(self).__name__} has no encoding')
        _l_(8865)
    self._body = body.encode(self._encoding)
    _l_(8867)
else:
    super()._set_body(body)
    _l_(8868)
