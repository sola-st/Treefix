# Extracted from ./data/repos/scrapy/scrapy/exporters.py
super().__init__(dont_fail=True, **kwargs)
self.file = file
self._kwargs.setdefault('ensure_ascii', not self.encoding)
self.encoder = ScrapyJSONEncoder(**self._kwargs)
