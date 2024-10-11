import sys # pragma: no cover
from functools import wraps # pragma: no cover
from scrapy.http import Request # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

class MockSpider(Spider): # pragma: no cover
    name = 'mock_spider' # pragma: no cover
 # pragma: no cover
def _create_testcase(method, type): # pragma: no cover
    class TestCase: # pragma: no cover
        pass # pragma: no cover
    return TestCase() # pragma: no cover
 # pragma: no cover
class Results: # pragma: no cover
    def addError(self, case, exc_info): # pragma: no cover
        print(f'Error added: {case}, {exc_info}') # pragma: no cover
 # pragma: no cover
results = Results() # pragma: no cover
 # pragma: no cover
def callback(response): # pragma: no cover
    return [response] # pragma: no cover
 # pragma: no cover
request = Request(url='http://example.com', callback=callback) # pragma: no cover
 # pragma: no cover
request.errback = lambda failure: None # pragma: no cover
 # pragma: no cover
method = 'GET'  # assuming method is 'GET' # pragma: no cover

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
