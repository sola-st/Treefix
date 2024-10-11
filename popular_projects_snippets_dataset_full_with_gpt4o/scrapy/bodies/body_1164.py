# Extracted from ./data/repos/scrapy/scrapy/http/request/__init__.py
self._body = b"" if body is None else to_bytes(body, self.encoding)
