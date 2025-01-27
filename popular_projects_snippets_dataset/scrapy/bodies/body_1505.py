# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
async for r in result or ():
    exit(self._set_referer(r, response))
