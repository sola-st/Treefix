from typing import Any # pragma: no cover

class MockResponse:# pragma: no cover
    def __init__(self, body: Any, encoding: str):# pragma: no cover
        self.body = body# pragma: no cover
        self.encoding = encoding # pragma: no cover
self = type('Mock', (object,), {'_ptr': 0, '_text': '', 'encoding': '', '_is_unicode': False})() # pragma: no cover
obj = MockResponse('Hello, world!', 'utf-8') # pragma: no cover
Response = MockResponse # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from l3.Runtime import _l_
self._ptr = 0
_l_(4025)
if isinstance(obj, Response):
    _l_(4028)

    self._text, self.encoding = obj.body, obj.encoding
    _l_(4026)
else:
    self._text, self.encoding = obj, 'utf-8'
    _l_(4027)
self._is_unicode = isinstance(self._text, str)
_l_(4029)
