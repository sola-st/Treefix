from unittest.mock import Mock # pragma: no cover
import logging # pragma: no cover

# Initializing request object with necessary attributes # pragma: no cover
request = Mock() # pragma: no cover
request.meta = {'redirect_ttl': 3, 'redirect_times': 1, 'redirect_urls': ['http://example.com'], 'redirect_reasons': ['TestReason']} # pragma: no cover
request.url = 'http://example.com' # pragma: no cover
request.dont_filter = False # pragma: no cover
request.priority = 1 # pragma: no cover
# Initializing self object with necessary attributes # pragma: no cover
self = Mock() # pragma: no cover
self.max_redirect_times = 5 # pragma: no cover
self.priority_adjust = 2 # pragma: no cover
# Initializing redirected object with necessary attributes # pragma: no cover
redirected = Mock() # pragma: no cover
redirected.meta = {} # pragma: no cover
# Initializing reason variable # pragma: no cover
reason = 'TestReason' # pragma: no cover
# Initializing logger object # pragma: no cover
logger = Mock() # pragma: no cover
logger.debug = logging.getLogger().debug # pragma: no cover
# Initializing spider object # pragma: no cover
spider = Mock() # pragma: no cover
# Initializing IgnoreRequest exception # pragma: no cover
IgnoreRequest = type('IgnoreRequest', (Exception,), {}) # pragma: no cover

import logging # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover

# Create a mock request object # pragma: no cover
class MockRequest: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.meta = {'redirect_ttl': 3, 'redirect_times': 0, 'redirect_urls': ['http://example.com'], 'redirect_reasons': ['temporary redirect']} # pragma: no cover
        self.url = 'http://example.com' # pragma: no cover
        self.dont_filter = False # pragma: no cover
        self.priority = 0 # pragma: no cover
 # pragma: no cover
# Create a mock self object # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.max_redirect_times = 5 # pragma: no cover
        self.priority_adjust = 1 # pragma: no cover
 # pragma: no cover
# Create a mock redirected object # pragma: no cover
class MockRedirected: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.meta = {} # pragma: no cover
        self.dont_filter = False # pragma: no cover
        self.priority = 0 # pragma: no cover
 # pragma: no cover
# Initialize the logging # pragma: no cover
logger = logging.getLogger('scrapy') # pragma: no cover
logger.setLevel(logging.DEBUG) # pragma: no cover
handler = logging.StreamHandler() # pragma: no cover
logger.addHandler(handler) # pragma: no cover
 # pragma: no cover
# Assign mock values to the variables # pragma: no cover
request = MockRequest() # pragma: no cover
self = MockSelf() # pragma: no cover
redirected = MockRedirected() # pragma: no cover
reason = 'temporary redirect' # pragma: no cover
spider = 'example_spider' # pragma: no cover

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
