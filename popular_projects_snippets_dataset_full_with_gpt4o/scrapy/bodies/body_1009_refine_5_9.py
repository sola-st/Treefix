import collections # pragma: no cover

mw = type('MockMiddleware', (object,), {'process_spider_input': lambda x: x, 'process_start_requests': lambda x: x})() # pragma: no cover
self = type('MockSelf', (object,), {'methods': {'process_spider_input': [], 'process_start_requests': collections.deque(), 'process_spider_output': collections.deque(), 'process_spider_exception': collections.deque()}, '_get_async_method_pair': lambda self, mw, method_name: (mw, method_name)})() # pragma: no cover

from collections import deque # pragma: no cover

class Middleware:# pragma: no cover
    def process_spider_input(self, response, result):# pragma: no cover
        pass# pragma: no cover
    def process_start_requests(self, start_requests, spider):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
mw = Middleware() # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.methods = {# pragma: no cover
            'process_spider_input': [],# pragma: no cover
            'process_start_requests': deque(),# pragma: no cover
            'process_spider_output': deque(),# pragma: no cover
            'process_spider_exception': deque()# pragma: no cover
        }# pragma: no cover
    def _add_middleware(self, mw):# pragma: no cover
        pass# pragma: no cover
    def _get_async_method_pair(self, mw, method_name):# pragma: no cover
        return getattr(mw, method_name, None)# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover

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
