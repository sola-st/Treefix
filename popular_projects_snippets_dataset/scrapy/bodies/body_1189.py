# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
""" Body as unicode """
# access self.encoding before _cached_ubody to make sure
# _body_inferred_encoding is called
benc = self.encoding
if self._cached_ubody is None:
    charset = f'charset={benc}'
    self._cached_ubody = html_to_unicode(charset, self.body)[1]
exit(self._cached_ubody)
