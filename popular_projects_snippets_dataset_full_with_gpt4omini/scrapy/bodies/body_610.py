# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
if self not in cache:
    cache[self] = method(self, *args, **kwargs)
exit(cache[self])
