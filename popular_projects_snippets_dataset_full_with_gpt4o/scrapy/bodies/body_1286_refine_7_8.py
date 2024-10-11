import logging # pragma: no cover
from scrapy.http import Request # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover

request = Request('http://example.com') # pragma: no cover
self = type('MockSelf', (object,), {'max_redirect_times': 5, 'priority_adjust': 10})() # pragma: no cover
redirected = Request('http://example.com/redirected') # pragma: no cover
reason = '301 Moved Permanently' # pragma: no cover
logger = logging.getLogger('scrapy') # pragma: no cover
spider = type('MockSpider', (object,), {})() # pragma: no cover
IgnoreRequest = IgnoreRequest # pragma: no cover

import logging # pragma: no cover
from types import SimpleNamespace # pragma: no cover

request = SimpleNamespace(meta={}, url='http://example.com', dont_filter=False, priority=0) # pragma: no cover
self = SimpleNamespace(max_redirect_times=5, priority_adjust=1) # pragma: no cover
redirected = SimpleNamespace(meta={}) # pragma: no cover
reason = 'some reason' # pragma: no cover
logger = logging.getLogger('scrapy.core.scraper') # pragma: no cover
spider = SimpleNamespace() # pragma: no cover
IgnoreRequest = type('IgnoreRequest', (Exception,), {}) # pragma: no cover

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
