import collections # pragma: no cover
from types import MethodType # pragma: no cover

self = type('Mock', (object,), {'methods': collections.defaultdict(collections.deque)})() # pragma: no cover
class Middleware: # pragma: no cover
    def process_spider_input(self): # pragma: no cover
        pass # pragma: no cover
    def process_start_requests(self): # pragma: no cover
        pass # pragma: no cover
mw = Middleware() # pragma: no cover
def super_add_middleware(mw): # pragma: no cover
    pass # pragma: no cover
self._get_async_method_pair = lambda mw, method_name: lambda x: x # pragma: no cover

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
