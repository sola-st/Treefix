# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
if self._exporting:
    self.exporter.finish_exporting()
    self._exporting = False
