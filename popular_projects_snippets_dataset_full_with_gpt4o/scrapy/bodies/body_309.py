# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
if b'Last-Modified' in cachedresponse.headers:
    request.headers[b'If-Modified-Since'] = cachedresponse.headers[b'Last-Modified']

if b'ETag' in cachedresponse.headers:
    request.headers[b'If-None-Match'] = cachedresponse.headers[b'ETag']
