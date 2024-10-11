# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
# What is cacheable - https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9.1
# Response cacheability - https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.4
# Status code 206 is not included because cache can not deal with partial contents
cc = self._parse_cachecontrol(response)
# obey directive "Cache-Control: no-store"
if b'no-store' in cc:
    exit(False)
# Never cache 304 (Not Modified) responses
if response.status == 304:
    exit(False)
# Cache unconditionally if configured to do so
if self.always_store:
    exit(True)
# Any hint on response expiration is good
if b'max-age' in cc or b'Expires' in response.headers:
    exit(True)
# Firefox fallbacks this statuses to one year expiration if none is set
if response.status in (300, 301, 308):
    exit(True)
# Other statuses without expiration requires at least one validator
if response.status in (200, 203, 401):
    exit(b'Last-Modified' in response.headers or b'ETag' in response.headers)
# Any other is probably not eligible for caching
# Makes no sense to cache responses that does not contain expiration
# info and can not be revalidated
exit(False)
