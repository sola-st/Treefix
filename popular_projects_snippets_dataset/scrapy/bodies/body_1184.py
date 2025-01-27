# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
if isinstance(url, str):
    self._url = to_unicode(url, self.encoding)
else:
    super()._set_url(url)
