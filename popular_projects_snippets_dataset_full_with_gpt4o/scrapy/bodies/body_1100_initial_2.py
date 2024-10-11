import sys # pragma: no cover

cb = lambda response, **kwargs: response # pragma: no cover
response = 'sample response' # pragma: no cover
cb_kwargs = {} # pragma: no cover
iterate_spider_output = lambda x: [x] # pragma: no cover
_create_testcase = lambda method, label: f'TestCase for {method} - {label}' # pragma: no cover
method = 'sample_method' # pragma: no cover
results = type('Mock', (object,), { 'addError': lambda self, case, exc_info: None })() # pragma: no cover
sys = type('Mock', (object,), { 'exc_info': lambda: ('exc_type', 'exc_value', 'exc_traceback') }) # pragma: no cover

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
