class MockSuperClass: # pragma: no cover
    def _set_body(self, body): # pragma: no cover
        print('Super _set_body called with:', body) # pragma: no cover

self = type('MockClass', (MockSuperClass,), {'_encoding': 'utf-8'})() # pragma: no cover
body = 'test string' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
self._body = b''  # used by encoding detection
_l_(19830)  # used by encoding detection
if isinstance(body, str):
    _l_(19835)

    if self._encoding is None:
        _l_(19832)

        raise TypeError('Cannot convert unicode body - '
                        f'{type(self).__name__} has no encoding')
        _l_(19831)
    self._body = body.encode(self._encoding)
    _l_(19833)
else:
    super()._set_body(body)
    _l_(19834)
