self = type('Mock', (object,), {'_ptr': 0, '_text': '', 'encoding': 'utf-8', '_is_unicode': False})() # pragma: no cover
obj = type('Mock', (object,), {'body': 'example body', 'encoding': 'utf-8'})() # pragma: no cover
Response = type('Response', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from l3.Runtime import _l_
self._ptr = 0
_l_(15551)
if isinstance(obj, Response):
    _l_(15554)

    self._text, self.encoding = obj.body, obj.encoding
    _l_(15552)
else:
    self._text, self.encoding = obj, 'utf-8'
    _l_(15553)
self._is_unicode = isinstance(self._text, str)
_l_(15555)
