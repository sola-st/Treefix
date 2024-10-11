import sys # pragma: no cover
from typing import Callable, Any, List, Dict # pragma: no cover

def cb(response: Any, **kwargs: Any) -> List[Any]: return [response] + list(kwargs.values()) # pragma: no cover
response = 'sample response' # pragma: no cover
cb_kwargs = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover
def iterate_spider_output(output: List[Any]) -> List[Any]: return output # pragma: no cover
def _create_testcase(method: str, name: str) -> str: return f'Testcase for {method} - {name}' # pragma: no cover
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
