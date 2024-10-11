from typing import Any, Dict, Union # pragma: no cover
from unittest.mock import Mock # pragma: no cover
from scrapy.http import Request, Response # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover
from collections import defaultdict # pragma: no cover

request = Request(url='http://example.com') # pragma: no cover
spider = Mock() # pragma: no cover
self = Mock() # pragma: no cover
self.policy = Mock() # pragma: no cover
self.policy.should_cache_request = Mock(return_value=True) # pragma: no cover
self.policy.is_cached_response_fresh = Mock(return_value=True) # pragma: no cover
self.storage = Mock() # pragma: no cover
self.storage.retrieve_response = Mock(return_value=Response(url='http://example.com')) # pragma: no cover
self.stats = Mock() # pragma: no cover
self.stats.inc_value = Mock() # pragma: no cover
self.ignore_missing = True # pragma: no cover
IgnoreRequest = IgnoreRequest # pragma: no cover

from collections import defaultdict # pragma: no cover
from types import SimpleNamespace # pragma: no cover
from scrapy.http import Response # pragma: no cover
from scrapy.exceptions import IgnoreRequest # pragma: no cover

request = SimpleNamespace(meta={}) # pragma: no cover
class CachePolicy:# pragma: no cover
    def should_cache_request(self, request):# pragma: no cover
        return True# pragma: no cover
    def is_cached_response_fresh(self, response, request):# pragma: no cover
        return True # pragma: no cover
class Storage:# pragma: no cover
    def retrieve_response(self, spider, request):# pragma: no cover
        response = Response(url='http://example.com', status=200, body=b'cached response')# pragma: no cover
        response.flags = []# pragma: no cover
        return response # pragma: no cover
class Stats:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.values = defaultdict(int)# pragma: no cover
    def inc_value(self, key, spider=None):# pragma: no cover
        self.values[key] += 1 # pragma: no cover
self = type('MockSelf', (object,), {# pragma: no cover
    'policy': CachePolicy(),# pragma: no cover
    'storage': Storage(),# pragma: no cover
    'stats': Stats(),# pragma: no cover
    'ignore_missing': False# pragma: no cover
})() # pragma: no cover
spider = SimpleNamespace() # pragma: no cover

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
