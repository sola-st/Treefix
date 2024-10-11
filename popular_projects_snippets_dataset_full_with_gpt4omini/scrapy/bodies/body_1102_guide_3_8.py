from functools import wraps # pragma: no cover
import sys # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MockRequest: pass # pragma: no cover
class MockResults: pass # pragma: no cover
results = MockResults() # pragma: no cover
results.addError = Mock() # pragma: no cover
method = 'GET' # pragma: no cover
request = MockRequest() # pragma: no cover
request.callback = Mock(side_effect=lambda response, **kwargs: 1 / 0)  # This will raise an exception # pragma: no cover
request.errback = Mock() # pragma: no cover
_create_testcase = Mock(return_value='testcase') # pragma: no cover
def iterate_spider_output(output): return output if isinstance(output, list) else [output] # pragma: no cover

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
