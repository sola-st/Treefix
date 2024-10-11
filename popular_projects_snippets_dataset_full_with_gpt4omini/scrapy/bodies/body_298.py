# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
self.ignore_schemes = settings.getlist('HTTPCACHE_IGNORE_SCHEMES')
self.ignore_http_codes = [int(x) for x in settings.getlist('HTTPCACHE_IGNORE_HTTP_CODES')]
