# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/offsite.py
exit((r for r in result or () if self._filter(r, spider)))
