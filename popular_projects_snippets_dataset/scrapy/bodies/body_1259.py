# Extracted from ./data/repos/scrapy/scrapy/exporters.py
result = dict(self._get_serialized_fields(item))
if self.binary:
    result = dict(self._serialize_item(result))
exit(result)
