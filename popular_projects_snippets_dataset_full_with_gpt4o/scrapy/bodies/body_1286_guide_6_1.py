import logging # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover

class MockRequest: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.meta = { # pragma: no cover
            'redirect_ttl': 3,  # Ensuring ttl > 0 # pragma: no cover
            'redirect_times': 2,  # Ensuring redirects <= self.max_redirect_times # pragma: no cover
            'redirect_urls': [], # pragma: no cover
            'redirect_reasons': [] # pragma: no cover
        } # pragma: no cover
        self.url = 'http://example.com' # pragma: no cover
        self.dont_filter = False # pragma: no cover
        self.priority = 0 # pragma: no cover
 # pragma: no cover
class MockRedirected: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.meta = {} # pragma: no cover
        self.dont_filter = False # pragma: no cover
        self.priority = 0 # pragma: no cover
 # pragma: no cover
class MockSpider: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.max_redirect_times = 5 # pragma: no cover
        self.priority_adjust = 1 # pragma: no cover
 # pragma: no cover
logging.basicConfig(level=logging.DEBUG) # pragma: no cover
logger = logging.getLogger(__name__) # pragma: no cover
 # pragma: no cover
request = MockRequest() # pragma: no cover
redirected = MockRedirected() # pragma: no cover
self = MockSelf() # pragma: no cover
spider = MockSpider() # pragma: no cover
reason = 'test_reason' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
ttl = request.meta.setdefault('redirect_ttl', self.max_redirect_times)
_l_(15557)
redirects = request.meta.get('redirect_times', 0) + 1
_l_(15558)

if ttl and redirects <= self.max_redirect_times:
    _l_(15567)

    redirected.meta['redirect_times'] = redirects
    _l_(15559)
    redirected.meta['redirect_ttl'] = ttl - 1
    _l_(15560)
    redirected.meta['redirect_urls'] = request.meta.get('redirect_urls', []) + [request.url]
    _l_(15561)
    redirected.meta['redirect_reasons'] = request.meta.get('redirect_reasons', []) + [reason]
    _l_(15562)
    redirected.dont_filter = request.dont_filter
    _l_(15563)
    redirected.priority = request.priority + self.priority_adjust
    _l_(15564)
    logger.debug("Redirecting (%(reason)s) to %(redirected)s from %(request)s",
                 {'reason': reason, 'redirected': redirected, 'request': request},
                 extra={'spider': spider})
    _l_(15565)
    aux = redirected
    _l_(15566)
    exit(aux)
logger.debug("Discarding %(request)s: max redirections reached",
             {'request': request}, extra={'spider': spider})
_l_(15568)
raise IgnoreRequest("max redirections reached")
_l_(15569)
