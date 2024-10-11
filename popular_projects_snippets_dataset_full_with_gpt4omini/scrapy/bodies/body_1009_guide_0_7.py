from collections import deque # pragma: no cover
from typing import Callable, Dict, Any # pragma: no cover

class MockMiddleware: # pragma: no cover
    def process_spider_input(self, response): pass # pragma: no cover
    def process_start_requests(self, request): pass # pragma: no cover
    def process_spider_output(self, response, request): return response # pragma: no cover
    def process_spider_exception(self, response, exception): pass # pragma: no cover
 # pragma: no cover
mocked_methods = { # pragma: no cover
    'process_spider_input': [], # pragma: no cover
    'process_start_requests': deque(), # pragma: no cover
    'process_spider_output': deque(), # pragma: no cover
    'process_spider_exception': deque() # pragma: no cover
} # pragma: no cover
 # pragma: no cover
mw = MockMiddleware() # pragma: no cover
self = type('MockSelf', (object,), {'methods': mocked_methods, '_get_async_method_pair': lambda mw, name: mw.process_spider_output})() # pragma: no cover

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
