# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
parsed = urlparse_cached(request)
self.scheme, self.netloc, self.host, self.port, self.path = _parsed_url_args(parsed)
proxy = request.meta.get('proxy')
if proxy:
    self.scheme, _, self.host, self.port, _ = _parse(proxy)
    self.path = self.url
