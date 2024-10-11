import logging # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover

request = type('Mock', (object,), {'meta': {}, 'url': 'http://example.com', 'dont_filter': False, 'priority': 0})() # pragma: no cover
self = type('Mock', (object,), {'max_redirect_times': 3, 'priority_adjust': 1})() # pragma: no cover
redirected = type('Mock', (object,), {'meta': {}, 'dont_filter': False, 'priority': 0})() # pragma: no cover
reason = 'mock reason' # pragma: no cover
logger = type('Mock', (object,), {'debug': lambda *args, **kwargs: None})() # pragma: no cover
spider = 'mock_spider' # pragma: no cover
IgnoreRequest = IgnoreRequest # pragma: no cover

import logging # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover

# Initialize the required Mock classes as necessary # pragma: no cover
request = type('Request', (object,), {'meta': {}, 'url': 'http://example.com', 'dont_filter': False, 'priority': 0})() # pragma: no cover
self = type('Self', (object,), {'max_redirect_times': 3, 'priority_adjust': 1})() # pragma: no cover
redirected = type('Redirected', (object,), {'meta': {}, 'dont_filter': False, 'priority': 0})() # pragma: no cover
reason = 'Temporary Redirect' # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
spider = 'test_spider' # pragma: no cover
IgnoreRequest = IgnoreRequest # pragma: no cover
# Ensuring the logger has a handler # pragma: no cover
if not logger.handlers: # pragma: no cover
    logger.addHandler(logging.StreamHandler()) # pragma: no cover

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
