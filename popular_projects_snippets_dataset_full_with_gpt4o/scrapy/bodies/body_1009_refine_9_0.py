from collections import deque # pragma: no cover

mw = type('MiddlewareMock', (object,), { 'process_spider_input': lambda x: x, 'process_start_requests': lambda x: x, 'process_spider_exception': lambda x: x })() # pragma: no cover
self = type('SelfMock', (object,), { 'methods': { 'process_spider_input': [], 'process_start_requests': deque(), 'process_spider_output': deque(), 'process_spider_exception': deque() }, '_get_async_method_pair': lambda self, mw, method_name: (lambda x: x) })() # pragma: no cover

from collections import deque # pragma: no cover

SelfBase = type('SelfBase', (object,), { '_add_middleware': lambda self, mw: None, '_get_async_method_pair': lambda self, mw, name: lambda x: x }) # pragma: no cover
self = type('SelfMock', (SelfBase,), { '__init__': lambda self: None })() # pragma: no cover
self.methods = { 'process_spider_input': [], 'process_start_requests': deque(), 'process_spider_output': deque(), 'process_spider_exception': deque() } # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
super()._add_middleware(mw)
_l_(16851)
if hasattr(mw, 'process_spider_input'):
    _l_(16853)

    self.methods['process_spider_input'].append(mw.process_spider_input)
    _l_(16852)
if hasattr(mw, 'process_start_requests'):
    _l_(16855)

    self.methods['process_start_requests'].appendleft(mw.process_start_requests)
    _l_(16854)
process_spider_output = self._get_async_method_pair(mw, 'process_spider_output')
_l_(16856)
self.methods['process_spider_output'].appendleft(process_spider_output)
_l_(16857)
process_spider_exception = getattr(mw, 'process_spider_exception', None)
_l_(16858)
self.methods['process_spider_exception'].appendleft(process_spider_exception)
_l_(16859)
