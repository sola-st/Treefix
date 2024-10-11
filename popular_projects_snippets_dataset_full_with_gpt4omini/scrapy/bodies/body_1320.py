# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcache.py
if not settings.getbool('HTTPCACHE_ENABLED'):
    raise NotConfigured
self.policy = load_object(settings['HTTPCACHE_POLICY'])(settings)
self.storage = load_object(settings['HTTPCACHE_STORAGE'])(settings)
self.ignore_missing = settings.getbool('HTTPCACHE_IGNORE_MISSING')
self.stats = stats
