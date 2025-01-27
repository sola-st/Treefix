# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
self._encoding = kwargs.pop('encoding', None)
self._cached_benc = None
self._cached_ubody = None
self._cached_selector = None
super().__init__(*args, **kwargs)
