from functools import wraps # pragma: no cover
import sys # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

class MockRequest: callback = None; errback = None # pragma: no cover
def mock_callback(response, **kwargs): return ['output'] # pragma: no cover
def mock_errback(failure): pass # pragma: no cover
results = type('MockResults', (object,), {'addError': lambda self, case, exc_info: None})() # pragma: no cover
method = 'GET' # pragma: no cover
request = MockRequest() # pragma: no cover
request.callback = mock_callback # pragma: no cover
request.errback = mock_errback # pragma: no cover
response = 'mock_response' # pragma: no cover
results = type('MockResults', (object,), {'addError': lambda self, case, exc_info: None})() # pragma: no cover
def iterate_spider_output(output): return output # pragma: no cover
def _create_testcase(method, callback_type): return 'testcase' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
from l3.Runtime import _l_
""" stop the request from returning objects and records any errors """

cb = request.callback
_l_(4557)

@wraps(cb)
def cb_wrapper(response, **cb_kwargs):
    _l_(4564)

    try:
        _l_(4563)

        output = cb(response, **cb_kwargs)
        _l_(4558)
        output = list(iterate_spider_output(output))
        _l_(4559)
    except Exception:
        _l_(4562)

        case = _create_testcase(method, 'callback')
        _l_(4560)
        results.addError(case, sys.exc_info())
        _l_(4561)

def eb_wrapper(failure):
    _l_(4568)

    case = _create_testcase(method, 'errback')
    _l_(4565)
    exc_info = failure.type, failure.value, failure.getTracebackObject()
    _l_(4566)
    results.addError(case, exc_info)
    _l_(4567)

request.callback = cb_wrapper
_l_(4569)
request.errback = eb_wrapper
_l_(4570)
