import sys # pragma: no cover

cb = lambda x, **kwargs: ['output1', 'output2'] # pragma: no cover
response = 'dummy_response' # pragma: no cover
cb_kwargs = {'key': 'value'} # pragma: no cover
iterate_spider_output = lambda x: (item for item in x) # pragma: no cover
_create_testcase = lambda m, c: f'TestCase for {m} {c}' # pragma: no cover
method = 'dummy_method' # pragma: no cover
results = type('Mock', (object,), {'addError': lambda self, case, exc_info: None})() # pragma: no cover
sys.exc_info = lambda: ('type', 'value', 'traceback') # pragma: no cover

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
