# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
old_reqs = self.requests.get(lvl, [])
self.requests[lvl] = old_reqs + new_reqs
