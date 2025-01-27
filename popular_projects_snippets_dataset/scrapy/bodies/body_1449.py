# Extracted from ./data/repos/scrapy/scrapy/resolver.py
if name in dnscache:
    exit(defer.succeed(dnscache[name]))
# in Twisted<=16.6, getHostByName() is always called with
# a default timeout of 60s (actually passed as (1, 3, 11, 45) tuple),
# so the input argument above is simply overridden
# to enforce Scrapy's DNS_TIMEOUT setting's value
timeout = (self.timeout,)
d = super().getHostByName(name, timeout)
if dnscache.limit:
    d.addCallback(self._cache_result, name)
exit(d)
