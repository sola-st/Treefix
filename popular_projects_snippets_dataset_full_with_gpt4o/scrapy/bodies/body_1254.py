# Extracted from ./data/repos/scrapy/scrapy/exporters.py
itemdict = dict(self._get_serialized_fields(item))
self.file.write(to_bytes(pprint.pformat(itemdict) + '\n'))
