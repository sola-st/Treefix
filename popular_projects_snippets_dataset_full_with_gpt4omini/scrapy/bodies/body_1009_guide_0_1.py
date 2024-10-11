from collections import deque # pragma: no cover
class Middleware: pass # pragma: no cover
class TestMiddleware: # pragma: no cover
    def process_spider_input(self, response): pass # pragma: no cover
    def process_start_requests(self, request): pass # pragma: no cover
    def process_spider_output(self, response): pass # pragma: no cover
    def process_spider_exception(self, response): pass # pragma: no cover

mw = TestMiddleware() # pragma: no cover
self = type('MockContext', (object,), {'methods': {'process_spider_input': [], 'process_start_requests': deque(), 'process_spider_output': deque(), 'process_spider_exception': deque()}})() # pragma: no cover
super = lambda: None # pragma: no cover
self._add_middleware = lambda mw: None # pragma: no cover
self._get_async_method_pair = lambda mw, name: getattr(mw, name) # pragma: no cover

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
