# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
lst = self.getlist(key)
lst.extend(self.normvalue(value))
self[key] = lst
