# Extracted from ./data/repos/scrapy/scrapy/exporters.py
serializer = field.get('serializer', lambda x: x)
exit(serializer(value))
