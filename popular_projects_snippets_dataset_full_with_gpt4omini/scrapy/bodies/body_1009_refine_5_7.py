from collections import deque # pragma: no cover

class MockMW:  # mock middleware class# pragma: no cover
    def process_spider_input(self, request):# pragma: no cover
        return request# pragma: no cover
    def process_start_requests(self, request):# pragma: no cover
        return request# pragma: no cover
    def process_spider_output(self, response):# pragma: no cover
        return response# pragma: no cover
    def process_spider_exception(self, exception):# pragma: no cover
        return exception# pragma: no cover
# pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.methods = {# pragma: no cover
            'process_spider_input': [],# pragma: no cover
            'process_start_requests': deque(),# pragma: no cover
            'process_spider_output': deque(),# pragma: no cover
            'process_spider_exception': deque()# pragma: no cover
        }# pragma: no cover
    def _get_async_method_pair(self, mw, method_name):# pragma: no cover
        return getattr(mw, method_name, None)# pragma: no cover
# pragma: no cover
mw = MockMW()# pragma: no cover
self = MockSelf() # pragma: no cover

from collections import deque # pragma: no cover

class MockMiddleware:  # mock middleware class# pragma: no cover
    def process_spider_input(self, request):# pragma: no cover
        return request# pragma: no cover
    def process_start_requests(self, requests):# pragma: no cover
        return requests# pragma: no cover
    def process_spider_output(self, response, request):# pragma: no cover
        return response# pragma: no cover
    def process_spider_exception(self, response, exception):# pragma: no cover
        return response# pragma: no cover
# pragma: no cover
class BaseClass:# pragma: no cover
    def _add_middleware(self, mw):# pragma: no cover
        pass  # Placeholder for the superclass method# pragma: no cover
# pragma: no cover
class MockSelf(BaseClass):  # Inheriting from the base class# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__()# pragma: no cover
        self.methods = {# pragma: no cover
            'process_spider_input': [],# pragma: no cover
            'process_start_requests': deque(),# pragma: no cover
            'process_spider_output': deque(),# pragma: no cover
            'process_spider_exception': deque()# pragma: no cover
        }# pragma: no cover
    def _get_async_method_pair(self, mw, method_name):# pragma: no cover
        return getattr(mw, method_name, None), getattr(mw, method_name, None)# pragma: no cover
# pragma: no cover
mw = MockMiddleware()  # Initialize mw# pragma: no cover
self = MockSelf()  # Initialize self # pragma: no cover

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
