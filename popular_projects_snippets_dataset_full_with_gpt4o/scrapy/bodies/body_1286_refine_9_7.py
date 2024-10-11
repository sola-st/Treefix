from unittest.mock import Mock # pragma: no cover
import logging # pragma: no cover

request = Mock() # pragma: no cover
request.meta = {} # pragma: no cover
request.url = 'http://example.com' # pragma: no cover
request.dont_filter = False # pragma: no cover
request.priority = 100 # pragma: no cover
self = Mock() # pragma: no cover
self.max_redirect_times = 10 # pragma: no cover
self.priority_adjust = 5 # pragma: no cover
redirected = Mock() # pragma: no cover
redirected.meta = {} # pragma: no cover
redirected.dont_filter = False # pragma: no cover
redirected.priority = 105 # pragma: no cover
reason = '301 Moved Permanently' # pragma: no cover
logger = Mock() # pragma: no cover
logger.debug = logging.debug # pragma: no cover
spider = Mock() # pragma: no cover
IgnoreRequest = type('IgnoreRequest', (Exception,), {}) # pragma: no cover

import logging # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover

class Request: # pragma: no cover
    def __init__(self, url): # pragma: no cover
        self.meta = {} # pragma: no cover
        self.url = url # pragma: no cover
        self.dont_filter = False # pragma: no cover
        self.priority = 0 # pragma: no cover
 # pragma: no cover
request = Request('http://example.com') # pragma: no cover
 # pragma: no cover
class Self: # pragma: no cover
    max_redirect_times = 5 # pragma: no cover
    priority_adjust = 1 # pragma: no cover
 # pragma: no cover
self = Self() # pragma: no cover
 # pragma: no cover
redirected = Request('http://example.com/redirected') # pragma: no cover
 # pragma: no cover
reason = '301 Moved Permanently' # pragma: no cover
 # pragma: no cover
logger = logging.getLogger('scrapy') # pragma: no cover
logger.addHandler(logging.StreamHandler()) # pragma: no cover
logger.setLevel(logging.DEBUG) # pragma: no cover
 # pragma: no cover
class Spider: # pragma: no cover
    name = 'example_spider' # pragma: no cover
 # pragma: no cover
spider = Spider() # pragma: no cover
 # pragma: no cover
IgnoreRequest = IgnoreRequest # pragma: no cover

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
