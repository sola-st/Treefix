# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
if not self._exporting:
    self.exporter.start_exporting()
    self._exporting = True
