class Response: # pragma: no cover
    def __init__(self, body, encoding): # pragma: no cover
        self.body = body # pragma: no cover
        self.encoding = encoding # pragma: no cover
obj = Response('Hello, world!', 'utf-8') # pragma: no cover
self = type('Mock', (object,), {'_ptr': 0, '_text': '', 'encoding': 'utf-8', '_is_unicode': False})() # pragma: no cover

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
