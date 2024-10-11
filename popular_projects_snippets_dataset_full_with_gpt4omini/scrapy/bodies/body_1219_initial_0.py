from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace(url='http://example.com', text='Example text', fragment='xyz', nofollow=True) # pragma: no cover
other = SimpleNamespace(url='http://example.com', text='Example text', fragment='xyz', nofollow=True) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/link.py
from l3.Runtime import _l_
aux = (
    self.url == other.url
    and self.text == other.text
    and self.fragment == other.fragment
    and self.nofollow == other.nofollow
)
_l_(6499)
exit(aux)
