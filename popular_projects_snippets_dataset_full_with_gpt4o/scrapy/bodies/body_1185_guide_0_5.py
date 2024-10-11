from typing import Optional # pragma: no cover

class MockSuperClass: # pragma: no cover
    def _set_body(self, body): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MyClass(MockSuperClass): # pragma: no cover
    def __init__(self, body: Optional[str] = None, encoding: Optional[str] = None): # pragma: no cover
        self._encoding = encoding # pragma: no cover
        self._body = b''  # used by encoding detection # pragma: no cover
        if isinstance(body, str): # pragma: no cover
            if self._encoding is None: # pragma: no cover
# uncovered # pragma: no cover
                raise TypeError('Cannot convert unicode body - ' # pragma: no cover
# uncovered # pragma: no cover
                              f'{type(self).__name__} has no encoding') # pragma: no cover
# uncovered # pragma: no cover
            self._body = body.encode(self._encoding) # pragma: no cover
        else: # pragma: no cover
# uncovered # pragma: no cover
            super()._set_body(body) # uncovered # pragma: no cover
 # pragma: no cover
# Example to execute uncovered path # pragma: no cover
try: # pragma: no cover
    instance = MyClass(body='test') # pragma: no cover
except TypeError as e: # pragma: no cover
    print(e) # pragma: no cover

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
