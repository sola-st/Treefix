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
