# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcache.py
if request.meta.get('dont_cache', False):
    exit(response)

# Skip cached responses and uncacheable requests
if 'cached' in response.flags or '_dont_cache' in request.meta:
    request.meta.pop('_dont_cache', None)
    exit(response)

# RFC2616 requires origin server to set Date header,
# https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.18
if 'Date' not in response.headers:
    response.headers['Date'] = formatdate(usegmt=True)

# Do not validate first-hand responses
cachedresponse = request.meta.pop('cached_response', None)
if cachedresponse is None:
    self.stats.inc_value('httpcache/firsthand', spider=spider)
    self._cache_response(spider, response, request, cachedresponse)
    exit(response)

if self.policy.is_cached_response_valid(cachedresponse, response, request):
    self.stats.inc_value('httpcache/revalidate', spider=spider)
    exit(cachedresponse)

self.stats.inc_value('httpcache/invalidate', spider=spider)
self._cache_response(spider, response, request, cachedresponse)
exit(response)
