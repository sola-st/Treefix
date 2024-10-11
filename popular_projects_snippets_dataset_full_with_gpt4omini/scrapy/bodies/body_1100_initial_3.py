import sys # pragma: no cover
from unittest.mock import Mock # pragma: no cover

cb = lambda response, **kwargs: response if kwargs.get('valid', True) else None # pragma: no cover
response = 'test_response' # pragma: no cover
cb_kwargs = {'valid': True} # pragma: no cover
def iterate_spider_output(output): return [output] # pragma: no cover
_create_testcase = lambda method, reason: f'Test case for {method} due to {reason}' # pragma: no cover
method = 'GET' # pragma: no cover
results = Mock(spec=set, addError=lambda case, exc_info: print(f'Error: {case}, Info: {exc_info}')) # pragma: no cover
sys = Mock(exc_info=lambda: ('type', 'value', 'traceback')) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
from l3.Runtime import _l_
try:
    _l_(9758)

    output = cb(response, **cb_kwargs)
    _l_(9753)
    output = list(iterate_spider_output(output))
    _l_(9754)
except Exception:
    _l_(9757)

    case = _create_testcase(method, 'callback')
    _l_(9755)
    results.addError(case, sys.exc_info())
    _l_(9756)
