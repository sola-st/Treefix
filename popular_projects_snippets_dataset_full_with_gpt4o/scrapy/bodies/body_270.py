# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
if format in self.exporters:
    exit(True)
logger.error("Unknown feed format: %(format)s", {'format': format})
