# Extracted from ./data/repos/scrapy/scrapy/item.py
self._values = {}
if args or kwargs:  # avoid creating dict for most common case
    for k, v in dict(*args, **kwargs).items():
        self[k] = v
