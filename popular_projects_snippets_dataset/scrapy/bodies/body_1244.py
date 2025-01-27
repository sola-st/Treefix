# Extracted from ./data/repos/scrapy/scrapy/exporters.py
serializer = field.get('serializer', self._join_if_needed)
exit(serializer(value))
