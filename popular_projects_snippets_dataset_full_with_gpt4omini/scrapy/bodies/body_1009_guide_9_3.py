from collections import defaultdict, deque # pragma: no cover

class MockMiddleware: # pragma: no cover
    def process_spider_input(self, response): return response # pragma: no cover
    def process_start_requests(self, request): return request # pragma: no cover
    def process_spider_output(self, response): return response # pragma: no cover
    def process_spider_exception(self, exception): return exception # pragma: no cover
 # pragma: no cover
mw = MockMiddleware() # pragma: no cover
self = type('MockSelf', (object,), {'methods': defaultdict(deque)})() # pragma: no cover
self._get_async_method_pair = lambda mw, name: getattr(mw, name) # pragma: no cover
self.methods['process_spider_input'] = deque() # pragma: no cover
self.methods['process_start_requests'] = deque() # pragma: no cover
self.methods['process_spider_output'] = deque() # pragma: no cover
self.methods['process_spider_exception'] = deque() # pragma: no cover
 # pragma: no cover
class MockSuper: # pragma: no cover
    def _add_middleware(self, mw): pass # pragma: no cover
super = MockSuper() # pragma: no cover

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
