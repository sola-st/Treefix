def cb(response, **kwargs): return 'callback executed' # pragma: no cover
response = {'data': 'sample response'} # pragma: no cover
cb_kwargs = {'key': 'value'} # pragma: no cover
def iterate_spider_output(output): return [output] # pragma: no cover
def _create_testcase(method, callback): return f'testcase for {method} with {callback}' # pragma: no cover
method = 'GET' # pragma: no cover

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
