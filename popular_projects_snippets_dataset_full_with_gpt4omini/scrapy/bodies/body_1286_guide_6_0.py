import logging # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover
from scrapy.http import Request # pragma: no cover

logging.basicConfig(level=logging.DEBUG) # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
self = type('MockSelf', (object,), {'max_redirect_times': 2, 'priority_adjust': 1})() # pragma: no cover
request = Request(url='http://example.com', meta={'redirect_ttl': 1, 'redirect_times': 0}) # pragma: no cover
reason = 'Redirecting to another URL' # pragma: no cover
redirected = Request(url='http://example.org') # pragma: no cover
redirected.dont_filter = False # pragma: no cover
redirected.priority = 0 # pragma: no cover
spider = 'test_spider' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
ttl = request.meta.setdefault('redirect_ttl', self.max_redirect_times)
_l_(4041)
redirects = request.meta.get('redirect_times', 0) + 1
_l_(4042)

if ttl and redirects <= self.max_redirect_times:
    _l_(4051)

    redirected.meta['redirect_times'] = redirects
    _l_(4043)
    redirected.meta['redirect_ttl'] = ttl - 1
    _l_(4044)
    redirected.meta['redirect_urls'] = request.meta.get('redirect_urls', []) + [request.url]
    _l_(4045)
    redirected.meta['redirect_reasons'] = request.meta.get('redirect_reasons', []) + [reason]
    _l_(4046)
    redirected.dont_filter = request.dont_filter
    _l_(4047)
    redirected.priority = request.priority + self.priority_adjust
    _l_(4048)
    logger.debug("Redirecting (%(reason)s) to %(redirected)s from %(request)s",
                 {'reason': reason, 'redirected': redirected, 'request': request},
                 extra={'spider': spider})
    _l_(4049)
    aux = redirected
    _l_(4050)
    exit(aux)
logger.debug("Discarding %(request)s: max redirections reached",
             {'request': request}, extra={'spider': spider})
_l_(4052)
raise IgnoreRequest("max redirections reached")
_l_(4053)
