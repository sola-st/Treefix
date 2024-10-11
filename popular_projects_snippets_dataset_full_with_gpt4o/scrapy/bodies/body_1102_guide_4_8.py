import sys # pragma: no cover
from functools import wraps # pragma: no cover

class MockResponse: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
def iterate_spider_output(output): # pragma: no cover
    if not hasattr(output, '__iter__') or isinstance(output, (str, bytes)): # pragma: no cover
        return [output] # pragma: no cover
    return list(output) # pragma: no cover
 # pragma: no cover
def _create_testcase(method, callback_type): # pragma: no cover
    return f'{method}_{callback_type}_testcase' # pragma: no cover
 # pragma: no cover
class MockResults: # pragma: no cover
    def addError(self, case, exc_info): # pragma: no cover
        print(f'Error added for {case} with exception {exc_info}') # pragma: no cover
 # pragma: no cover
results = MockResults() # pragma: no cover
 # pragma: no cover
class MockRequest: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.callback = self.mock_callback # pragma: no cover
        self.errback = self.mock_errback # pragma: no cover
 # pragma: no cover
    def mock_callback(self, response, **cb_kwargs): # pragma: no cover
        raise Exception('Simulated callback error') # pragma: no cover
 # pragma: no cover
    def mock_errback(self, failure): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
request = MockRequest() # pragma: no cover
method = 'GET' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
from l3.Runtime import _l_
""" stop the request from returning objects and records any errors """

cb = request.callback
_l_(15910)

@wraps(cb)
def cb_wrapper(response, **cb_kwargs):
    _l_(15917)

    try:
        _l_(15916)

        output = cb(response, **cb_kwargs)
        _l_(15911)
        output = list(iterate_spider_output(output))
        _l_(15912)
    except Exception:
        _l_(15915)

        case = _create_testcase(method, 'callback')
        _l_(15913)
        results.addError(case, sys.exc_info())
        _l_(15914)

def eb_wrapper(failure):
    _l_(15921)

    case = _create_testcase(method, 'errback')
    _l_(15918)
    exc_info = failure.type, failure.value, failure.getTracebackObject()
    _l_(15919)
    results.addError(case, exc_info)
    _l_(15920)

request.callback = cb_wrapper
_l_(15922)
request.errback = eb_wrapper
_l_(15923)
