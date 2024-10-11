import sys # pragma: no cover

cb = lambda response, **kwargs: 'sample_output' # pragma: no cover
response = 'sample_response' # pragma: no cover
cb_kwargs = {'key': 'value'} # pragma: no cover
iterate_spider_output = lambda output: iter([output]) # pragma: no cover
_create_testcase = lambda method, type: 'test_case' # pragma: no cover
method = 'GET' # pragma: no cover
results = type('Mock', (object,), {'addError': lambda self, case, exc_info: 'error_added'})() # pragma: no cover
sys = type('Mock', (object,), {'exc_info': lambda: ('type', 'value', 'traceback')}) # pragma: no cover

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
