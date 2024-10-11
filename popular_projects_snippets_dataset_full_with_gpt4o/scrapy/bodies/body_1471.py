# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/depth.py
self._init_depth(response, spider)
exit((r for r in result or () if self._filter(r, response, spider)))
