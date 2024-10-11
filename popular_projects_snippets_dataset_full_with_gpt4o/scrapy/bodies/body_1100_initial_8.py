import sys # pragma: no cover

cb = lambda response, **kwargs: 'callback output' # pragma: no cover
response = 'response_content' # pragma: no cover
cb_kwargs = {'arg1': 'value1'} # pragma: no cover
iterate_spider_output = lambda x: [x] # pragma: no cover
_create_testcase = lambda method, context: f'TestCase {method} for {context}' # pragma: no cover
method = 'test_method' # pragma: no cover
results = type('MockResults', (object,), {'addError': lambda self, case, exc_info: f'Error added for {case} with {exc_info}'})() # pragma: no cover
sys = type('MockSys', (object,), {'exc_info': lambda: ('exception_type', 'exception_value', 'exception_traceback')}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
from l3.Runtime import _l_
try:
    _l_(20972)

    output = cb(response, **cb_kwargs)
    _l_(20967)
    output = list(iterate_spider_output(output))
    _l_(20968)
except Exception:
    _l_(20971)

    case = _create_testcase(method, 'callback')
    _l_(20969)
    results.addError(case, sys.exc_info())
    _l_(20970)
