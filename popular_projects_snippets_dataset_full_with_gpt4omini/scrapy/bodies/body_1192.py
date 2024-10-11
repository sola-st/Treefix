# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
if self._cached_benc is None:
    content_type = to_unicode(self.headers.get(b'Content-Type', b''))
    benc, ubody = html_to_unicode(content_type, self.body,
                                  auto_detect_fun=self._auto_detect_fun,
                                  default_encoding=self._DEFAULT_ENCODING)
    self._cached_benc = benc
    self._cached_ubody = ubody
exit(self._cached_benc)
