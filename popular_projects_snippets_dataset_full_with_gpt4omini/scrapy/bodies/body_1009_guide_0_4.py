from collections import deque # pragma: no cover
import asyncio # pragma: no cover

class MockMiddleware:  # pragma: no cover
    def process_spider_input(self, response): pass # pragma: no cover
    def process_start_requests(self, request): pass # pragma: no cover
    async def process_spider_output(self, response, result): pass # pragma: no cover
    async def process_spider_exception(self, response, exception): pass # pragma: no cover
class Mock:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.methods = { # pragma: no cover
            'process_spider_input': [], # pragma: no cover
            'process_start_requests': deque(), # pragma: no cover
            'process_spider_output': deque(), # pragma: no cover
            'process_spider_exception': deque() # pragma: no cover
        } # pragma: no cover
        self._add_middleware(MockMiddleware()) # pragma: no cover
    def _add_middleware(self, mw):  # pragma: no cover
        self.methods['process_spider_input'].append(mw.process_spider_input)  # pragma: no cover
        self.methods['process_start_requests'].appendleft(mw.process_start_requests)  # pragma: no cover
        process_spider_output = mw.process_spider_output  # pragma: no cover
        self.methods['process_spider_output'].appendleft(process_spider_output)  # pragma: no cover
        process_spider_exception = mw.process_spider_exception  # pragma: no cover
        self.methods['process_spider_exception'].appendleft(process_spider_exception)  # pragma: no cover

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
