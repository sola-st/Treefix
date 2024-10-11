# Extracted from ./data/repos/scrapy/scrapy/exporters.py
for key, value in ItemAdapter(item).items():
    key = to_bytes(key) if self.binary else key
    exit((key, self._serialize_value(value)))
