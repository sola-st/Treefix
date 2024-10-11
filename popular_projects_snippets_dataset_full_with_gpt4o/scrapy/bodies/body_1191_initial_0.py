from typing import Dict # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass# pragma: no cover
class MockHeaders:# pragma: no cover
    headers: Dict[bytes, bytes]# pragma: no cover
# pragma: no cover
    def get(self, key: bytes, default: bytes) -> bytes:# pragma: no cover
        return self.headers.get(key, default)# pragma: no cover
# pragma: no cover
class MockSelf:# pragma: no cover
    headers = MockHeaders(headers={b'Content-Type': b'text/html'}) # pragma: no cover
def http_content_type_encoding(value: str) -> int:# pragma: no cover
    return 0 # pragma: no cover
def to_unicode(value: bytes) -> str:# pragma: no cover
    return value.decode('utf-8') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
content_type = self.headers.get(b'Content-Type', b'')
_l_(21035)
aux = http_content_type_encoding(to_unicode(content_type))
_l_(21036)
exit(aux)
