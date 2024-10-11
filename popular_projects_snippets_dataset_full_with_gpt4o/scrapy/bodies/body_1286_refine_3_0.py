from collections import defaultdict # pragma: no cover
import logging # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover

request = type('Request', (object,), {'meta': defaultdict(int), 'dont_filter': False, 'priority': 0, 'url': 'http://example.com'})() # pragma: no cover
self = type('Self', (object,), {'max_redirect_times': 3, 'priority_adjust': 1})() # pragma: no cover
redirected = type('Redirected', (object,), {'meta': defaultdict(list), 'dont_filter': False, 'priority': 0})() # pragma: no cover
reason = '301 Moved Permanently' # pragma: no cover
logger = logging.getLogger('scrapy.core.scraper') # pragma: no cover
spider = type('Spider', (object,), {})() # pragma: no cover

from collections import defaultdict # pragma: no cover
import logging # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover

class Request: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.meta = defaultdict(dict) # pragma: no cover
        self.url = 'http://example.com' # pragma: no cover
        self.dont_filter = False # pragma: no cover
        self.priority = 0 # pragma: no cover
 # pragma: no cover
class Self: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.max_redirect_times = 3 # pragma: no cover
        self.priority_adjust = 1 # pragma: no cover
 # pragma: no cover
class Redirected: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.meta = defaultdict(dict) # pragma: no cover
        self.dont_filter = False # pragma: no cover
        self.priority = 0 # pragma: no cover
 # pragma: no cover
class Logger: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.logger = logging.getLogger('test_logger') # pragma: no cover
    def debug(self, msg, *args, **kwargs): # pragma: no cover
        self.logger.debug(msg, *args, **kwargs) # pragma: no cover
 # pragma: no cover
request = Request() # pragma: no cover
self = Self() # pragma: no cover
redirected = Redirected() # pragma: no cover
reason = 'Example Reason' # pragma: no cover
logger = Logger() # pragma: no cover
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
