from functools import wraps # pragma: no cover
from twisted.internet import defer # pragma: no cover
import sys # pragma: no cover

class MockRequest:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.callback = None# pragma: no cover
        self.errback = None# pragma: no cover
request = MockRequest() # pragma: no cover
def mock_iterate_spider_output(output):# pragma: no cover
    if isinstance(output, list):# pragma: no cover
        return output# pragma: no cover
    return [output]# pragma: no cover
iterate_spider_output = mock_iterate_spider_output # pragma: no cover
def _create_testcase(method, callback_type):# pragma: no cover
    return f'Testcase(method={method}, type={callback_type})'# pragma: no cover
_create_testcase = _create_testcase # pragma: no cover
method = 'GET' # pragma: no cover
class MockResults:# pragma: no cover
    def addError(self, case, exc_info):# pragma: no cover
        print(f'Error added: {case}, Info: {exc_info}')# pragma: no cover
results = MockResults() # pragma: no cover
class MockFailure:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value# pragma: no cover
    def getTracebackObject(self):# pragma: no cover
        return 'Traceback'# pragma: no cover
# pragma: no cover
def mock_failure_handler():# pragma: no cover
    return MockFailure(Exception, 'Error occurred')# pragma: no cover
event_loop = mock_failure_handler()# pragma: no cover
 # pragma: no cover

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
