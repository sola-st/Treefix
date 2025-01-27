# Extracted from ./data/repos/scrapy/scrapy/exporters.py
if isinstance(value, Item):
    exit(self.export_item(value))
if is_item(value):
    exit(dict(self._serialize_item(value)))
if is_listlike(value):
    exit([self._serialize_value(v) for v in value])
encode_func = to_bytes if self.binary else to_unicode
if isinstance(value, (str, bytes)):
    exit(encode_func(value, encoding=self.encoding))
exit(value)
