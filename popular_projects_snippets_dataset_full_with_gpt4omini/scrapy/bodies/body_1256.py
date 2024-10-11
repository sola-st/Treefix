# Extracted from ./data/repos/scrapy/scrapy/exporters.py
serializer = field.get('serializer', self._serialize_value)
exit(serializer(value))
