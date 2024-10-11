# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
self.file = file
self.exporter = exporter
self.storage = storage
# feed params
self.batch_id = batch_id
self.format = format
self.store_empty = store_empty
self.uri_template = uri_template
self.uri = uri
self.filter = filter
# flags
self.itemcount = 0
self._exporting = False
