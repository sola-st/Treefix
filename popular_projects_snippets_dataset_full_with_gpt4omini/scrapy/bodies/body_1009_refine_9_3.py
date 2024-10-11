from collections import defaultdict, deque # pragma: no cover

class MockMiddleware: pass # pragma: no cover
mw = MockMiddleware() # pragma: no cover
mw.process_spider_input = lambda request: request # pragma: no cover
mw.process_start_requests = deque() # pragma: no cover
def mock_get_async_method_pair(mw, method_name): return lambda *args: None, lambda *args: None # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self.methods = defaultdict(deque) # pragma: no cover
self._get_async_method_pair = mock_get_async_method_pair # pragma: no cover
self.methods['process_spider_output'] = deque() # pragma: no cover
self.methods['process_spider_exception'] = deque() # pragma: no cover

from collections import defaultdict, deque # pragma: no cover

class Base:# pragma: no cover
    def _add_middleware(self, mw):# pragma: no cover
        pass  # Placeholder for base class middleware addition# pragma: no cover
# pragma: no cover
class MockMiddleware:# pragma: no cover
    def process_spider_input(self, request):# pragma: no cover
        pass# pragma: no cover
    def process_start_requests(self):# pragma: no cover
        pass# pragma: no cover
    def process_spider_output(self):# pragma: no cover
        pass# pragma: no cover
    def process_spider_exception(self, exception):# pragma: no cover
        pass # pragma: no cover
mw = MockMiddleware() # pragma: no cover
self = Base()  # Instance of the base class # pragma: no cover
self.methods = defaultdict(deque)# pragma: no cover
self.methods['process_spider_input'] = []# pragma: no cover
self.methods['process_start_requests'] = deque()# pragma: no cover
self.methods['process_spider_output'] = deque()# pragma: no cover
self.methods['process_spider_exception'] = deque() # pragma: no cover
def mock_get_async_method_pair(mw, method_name):# pragma: no cover
    return mw.process_spider_output, mw.process_spider_output# pragma: no cover
self._get_async_method_pair = mock_get_async_method_pair # pragma: no cover

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
