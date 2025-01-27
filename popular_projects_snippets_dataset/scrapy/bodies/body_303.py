# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
self.always_store = settings.getbool('HTTPCACHE_ALWAYS_STORE')
self.ignore_schemes = settings.getlist('HTTPCACHE_IGNORE_SCHEMES')
self._cc_parsed = WeakKeyDictionary()
self.ignore_response_cache_controls = [
    to_bytes(cc) for cc in settings.getlist('HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS')
]
