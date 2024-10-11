import sys # pragma: no cover
from functools import wraps # pragma: no cover

class MockResponse: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockFailure: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.type = Exception # pragma: no cover
        self.value = Exception('Mock exception') # pragma: no cover
    def getTracebackObject(self): # pragma: no cover
        return None # pragma: no cover
 # pragma: no cover
def iterate_spider_output(output): # pragma: no cover
    if isinstance(output, list): # pragma: no cover
        return output # pragma: no cover
    return [output] # pragma: no cover
 # pragma: no cover
def _create_testcase(method, callback_type): # pragma: no cover
    return f'{method} {callback_type}' # pragma: no cover
 # pragma: no cover
class MockResults: # pragma: no cover
    def addError(self, case, exc_info): # pragma: no cover
        print(f'Error added: {case}, {exc_info}') # pragma: no cover
 # pragma: no cover
results = MockResults() # pragma: no cover
 # pragma: no cover
def mock_callback(response, **cb_kwargs): # pragma: no cover
    raise Exception('Simulated callback exception') # pragma: no cover
 # pragma: no cover
def mock_errback(failure): # pragma: no cover
    raise Exception('Simulated errback exception') # pragma: no cover
 # pragma: no cover
request = type('MockRequest', (object,), { # pragma: no cover
    'callback': mock_callback, # pragma: no cover
    'errback': mock_errback # pragma: no cover
})() # pragma: no cover
method = 'GET' # pragma: no cover
response = MockResponse() # pragma: no cover
failure = MockFailure() # pragma: no cover

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
