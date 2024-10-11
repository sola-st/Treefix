request = type('MockRequest', (object,), {'callback': lambda response, **cb_kwargs: None, 'errback': lambda failure: None})() # pragma: no cover
iterate_spider_output = lambda output: output # pragma: no cover
_create_testcase = lambda method, type: f'Testcase for {method} with {type}' # pragma: no cover
method = 'test_method' # pragma: no cover
results = type('MockResults', (object,), {'addError': lambda self, case, exc_info: print(f'Error added for {case}: {exc_info}')})() # pragma: no cover

request = type('MockRequest', (object,), {'callback': lambda response, **cb_kwargs: None, 'errback': lambda failure: None})() # pragma: no cover
iterate_spider_output = lambda output: output # pragma: no cover
_create_testcase = lambda method, type: f'Testcase for {method} with {type}' # pragma: no cover
method = 'test_method' # pragma: no cover
results = type('MockResults', (object,), {'addError': lambda self, case, exc_info: print(f'Error added for {case}: {exc_info}')})() # pragma: no cover

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
