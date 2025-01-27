# Extracted from ./data/repos/scrapy/scrapy/exporters.py
itemdict = dict(self._get_serialized_fields(item))
data = self.encoder.encode(itemdict) + '\n'
self.file.write(to_bytes(data, self.encoding))
