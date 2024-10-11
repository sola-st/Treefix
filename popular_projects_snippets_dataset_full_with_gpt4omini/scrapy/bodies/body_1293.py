# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpauth.py
auth = getattr(self, 'auth', None)
if auth and b'Authorization' not in request.headers:
    domain = urlparse_cached(request).hostname
    if self.domain_unset:
        self.domain = domain
        self.domain_unset = False
    if not self.domain or url_is_from_any_domain(request.url, [self.domain]):
        request.headers[b'Authorization'] = auth
