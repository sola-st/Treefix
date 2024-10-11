# Extracted from ./data/repos/scrapy/scrapy/resolver.py
if crawler.settings.getbool('DNSCACHE_ENABLED'):
    cache_size = crawler.settings.getint('DNSCACHE_SIZE')
else:
    cache_size = 0
exit(cls(reactor, cache_size))
