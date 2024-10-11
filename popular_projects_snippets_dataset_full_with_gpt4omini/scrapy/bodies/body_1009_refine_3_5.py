from collections import defaultdict, deque # pragma: no cover

class Base:# pragma: no cover
    def _add_middleware(self, mw): pass # pragma: no cover
class MockMiddleware:# pragma: no cover
    def process_spider_input(self, request): pass# pragma: no cover
    def process_start_requests(self): pass# pragma: no cover
    def process_spider_output(self): pass# pragma: no cover
    def process_spider_exception(self, exception): pass # pragma: no cover
class Mock(Base):# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__()# pragma: no cover
        self.methods = defaultdict(deque)# pragma: no cover
    def _get_async_method_pair(self, mw, method_name): return mw.process_spider_output # pragma: no cover
mw = MockMiddleware() # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
super()._add_middleware(mw)
_l_(5223)
if hasattr(mw, 'process_spider_input'):
    _l_(5225)

    self.methods['process_spider_input'].append(mw.process_spider_input)
    _l_(5224)
if hasattr(mw, 'process_start_requests'):
    _l_(5227)

    self.methods['process_start_requests'].appendleft(mw.process_start_requests)
    _l_(5226)
process_spider_output = self._get_async_method_pair(mw, 'process_spider_output')
_l_(5228)
self.methods['process_spider_output'].appendleft(process_spider_output)
_l_(5229)
process_spider_exception = getattr(mw, 'process_spider_exception', None)
_l_(5230)
self.methods['process_spider_exception'].appendleft(process_spider_exception)
_l_(5231)
