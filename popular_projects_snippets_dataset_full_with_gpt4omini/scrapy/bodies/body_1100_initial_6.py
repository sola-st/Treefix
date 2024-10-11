import sys # pragma: no cover
from unittest.mock import Mock # pragma: no cover

cb = lambda x, **kwargs: x # pragma: no cover
response = 'sample response' # pragma: no cover
cb_kwargs = {'key': 'value'} # pragma: no cover
def iterate_spider_output(output): return output if isinstance(output, list) else [output] # pragma: no cover
_create_testcase = lambda method, name: f'TestCase({method}, {name})' # pragma: no cover
method = 'GET' # pragma: no cover
results = Mock() # pragma: no cover
results.addError = Mock() # pragma: no cover

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
