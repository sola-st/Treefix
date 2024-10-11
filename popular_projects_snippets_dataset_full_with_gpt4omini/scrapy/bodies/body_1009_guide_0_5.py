from collections import defaultdict, deque # pragma: no cover
from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
self.methods = defaultdict(deque) # pragma: no cover
mw = SimpleNamespace() # pragma: no cover
mw.process_spider_input = lambda x: x # pragma: no cover
mw.process_start_requests = lambda x: x # pragma: no cover
mw.process_spider_output = lambda x: x # pragma: no cover
mw.process_spider_exception = lambda x: x # pragma: no cover

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
