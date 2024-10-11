# Extracted from ./data/repos/scrapy/scrapy/exporters.py
super().__init__(dont_fail=True, **kwargs)
self.file = file
# there is a small difference between the behaviour or JsonItemExporter.indent
# and ScrapyJSONEncoder.indent. ScrapyJSONEncoder.indent=None is needed to prevent
# the addition of newlines everywhere
json_indent = self.indent if self.indent is not None and self.indent > 0 else None
self._kwargs.setdefault('indent', json_indent)
self._kwargs.setdefault('ensure_ascii', not self.encoding)
self.encoder = ScrapyJSONEncoder(**self._kwargs)
self.first_item = True
