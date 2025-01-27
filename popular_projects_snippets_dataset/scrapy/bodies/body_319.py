# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
self.cachedir = data_path(settings['HTTPCACHE_DIR'])
self.expiration_secs = settings.getint('HTTPCACHE_EXPIRATION_SECS')
self.use_gzip = settings.getbool('HTTPCACHE_GZIP')
self._open = gzip.open if self.use_gzip else open
