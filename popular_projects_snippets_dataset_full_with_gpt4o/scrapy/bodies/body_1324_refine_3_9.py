from collections import defaultdict # pragma: no cover
from types import SimpleNamespace # pragma: no cover
from datetime import datetime, timedelta # pragma: no cover

request = SimpleNamespace(meta={'dont_cache': False}) # pragma: no cover
self = SimpleNamespace(policy=type('Mock', (object,), {'should_cache_request': lambda r: True, 'is_cached_response_fresh': lambda resp, req: True})(), storage=type('Mock', (object,), {'retrieve_response': lambda s, r: None})(), stats=type('Mock', (object,), {'inc_value': lambda metric, spider: None})(), ignore_missing=False) # pragma: no cover
spider = SimpleNamespace() # pragma: no cover
IgnoreRequest = type('IgnoreRequest', (Exception,), {}) # pragma: no cover

from collections import defaultdict # pragma: no cover
from types import SimpleNamespace # pragma: no cover

request = SimpleNamespace(meta={'dont_cache': False}) # pragma: no cover
self = SimpleNamespace(policy=type('MockPolicy', (object,), {'should_cache_request': lambda self, request: True, 'is_cached_response_fresh': lambda self, cachedresponse, request: True})(), storage=type('MockStorage', (object,), {'retrieve_response': lambda self, spider, request: type('MockResponse', (object,), {'flags': [], '__copy__': lambda self: self})()})(), stats=type('MockStats', (object,), {'inc_value': lambda self, value, spider=None: None})(), ignore_missing=False) # pragma: no cover
spider = 'mock_spider' # pragma: no cover
IgnoreRequest = type('IgnoreRequest', (Exception,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcache.py
from l3.Runtime import _l_
if request.meta.get('dont_cache', False):
    _l_(21085)

    aux = None
    _l_(21084)
    exit(aux)

# Skip uncacheable requests
if not self.policy.should_cache_request(request):
    _l_(21088)

    request.meta['_dont_cache'] = True  # flag as uncacheable
    _l_(21086)  # flag as uncacheable
    aux = None
    _l_(21087)
    exit(aux)

# Look for cached response and check if expired
cachedresponse = self.storage.retrieve_response(spider, request)
_l_(21089)
if cachedresponse is None:
    _l_(21095)

    self.stats.inc_value('httpcache/miss', spider=spider)
    _l_(21090)
    if self.ignore_missing:
        _l_(21093)

        self.stats.inc_value('httpcache/ignore', spider=spider)
        _l_(21091)
        raise IgnoreRequest(f"Ignored request not in cache: {request}")
        _l_(21092)
    aux = None  # first time request
    _l_(21094)  # first time request
    exit(aux)  # first time request

# Return cached response only if not expired
cachedresponse.flags.append('cached')
_l_(21096)
if self.policy.is_cached_response_fresh(cachedresponse, request):
    _l_(21099)

    self.stats.inc_value('httpcache/hit', spider=spider)
    _l_(21097)
    aux = cachedresponse
    _l_(21098)
    exit(aux)

# Keep a reference to cached response to avoid a second cache lookup on
# process_response hook
request.meta['cached_response'] = cachedresponse
_l_(21100)
aux = None
_l_(21101)

exit(aux)
