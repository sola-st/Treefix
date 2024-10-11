# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/offsite.py
async for r in result or ():
    if self._filter(r, spider):
        exit(r)
