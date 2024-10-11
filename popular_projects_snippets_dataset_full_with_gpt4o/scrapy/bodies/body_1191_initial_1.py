from typing import Dict, Any # pragma: no cover
import sys # pragma: no cover

class MockHeaders(Dict[bytes, bytes]): # pragma: no cover
    def get(self, key: bytes, default: bytes) -> bytes: # pragma: no cover
        if key == b'Content-Type': # pragma: no cover
            return b'text/html; charset=UTF-8' # pragma: no cover
        return default # pragma: no cover
class MockSelf: # pragma: no cover
    headers: Any = MockHeaders() # pragma: no cover
self = MockSelf() # pragma: no cover
def http_content_type_encoding(arg: str) -> int: # pragma: no cover
    return 0 if arg == 'text/html; charset=UTF-8' else 1 # pragma: no cover
def to_unicode(arg: bytes) -> str: # pragma: no cover
    return arg.decode('utf-8') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
content_type = self.headers.get(b'Content-Type', b'')
_l_(21035)
aux = http_content_type_encoding(to_unicode(content_type))
_l_(21036)
exit(aux)
