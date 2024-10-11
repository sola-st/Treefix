self = type('Mock', (object,), {'_body': b'', '_encoding': 'utf-8', '_set_body': lambda self, body: None})() # pragma: no cover
body = 'test' # pragma: no cover

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
