# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
self.headers = Headers(headers or {})
self.status = int(status)
self._set_body(body)
self._set_url(url)
self.request = request
self.flags = [] if flags is None else list(flags)
self.certificate = certificate
self.ip_address = ip_address
self.protocol = protocol
