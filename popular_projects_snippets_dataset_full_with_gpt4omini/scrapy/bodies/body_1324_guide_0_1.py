from scrapy.exceptions import IgnoreRequest # pragma: no cover
from scrapy.http import Request # pragma: no cover

request = Request(url='http://example.com') # pragma: no cover
self = type('Mock', (), {'policy': type('Mock', (), {'should_cache_request': lambda self, req: True, 'is_cached_response_fresh': lambda self, resp, req: True}), 'storage': type('Mock', (), {'retrieve_response': lambda self, spider, req: None}), 'stats': type('Mock', (), {'inc_value': lambda self, stat, spider: None}), 'ignore_missing': True})() # pragma: no cover
spider = 'example_spider' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcache.py
from l3.Runtime import _l_
if request.meta.get('dont_cache', False):
    _l_(9642)

    aux = None
    _l_(9641)
    exit(aux)

# Skip uncacheable requests
if not self.policy.should_cache_request(request):
    _l_(9645)

    request.meta['_dont_cache'] = True  # flag as uncacheable
    _l_(9643)  # flag as uncacheable
    aux = None
    _l_(9644)
    exit(aux)

# Look for cached response and check if expired
cachedresponse = self.storage.retrieve_response(spider, request)
_l_(9646)
if cachedresponse is None:
    _l_(9652)

    self.stats.inc_value('httpcache/miss', spider=spider)
    _l_(9647)
    if self.ignore_missing:
        _l_(9650)

        self.stats.inc_value('httpcache/ignore', spider=spider)
        _l_(9648)
        raise IgnoreRequest(f"Ignored request not in cache: {request}")
        _l_(9649)
    aux = None  # first time request
    _l_(9651)  # first time request
    exit(aux)  # first time request

# Return cached response only if not expired
cachedresponse.flags.append('cached')
_l_(9653)
if self.policy.is_cached_response_fresh(cachedresponse, request):
    _l_(9656)

    self.stats.inc_value('httpcache/hit', spider=spider)
    _l_(9654)
    aux = cachedresponse
    _l_(9655)
    exit(aux)

# Keep a reference to cached response to avoid a second cache lookup on
# process_response hook
request.meta['cached_response'] = cachedresponse
_l_(9657)
aux = None
_l_(9658)

exit(aux)
