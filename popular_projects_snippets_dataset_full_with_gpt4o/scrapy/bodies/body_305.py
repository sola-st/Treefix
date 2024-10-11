# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
if urlparse_cached(request).scheme in self.ignore_schemes:
    exit(False)
cc = self._parse_cachecontrol(request)
# obey user-agent directive "Cache-Control: no-store"
if b'no-store' in cc:
    exit(False)
# Any other is eligible for caching
exit(True)
