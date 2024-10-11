from scrapy import Selector # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.selector = Selector(text='<html><body><p>Hello, world!</p></body></html>') # pragma: no cover
query = 'p::text' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
from l3.Runtime import _l_
aux = self.selector.css(query)
_l_(20897)
exit(aux)
