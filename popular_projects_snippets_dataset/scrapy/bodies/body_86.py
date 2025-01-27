# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
self._rules = []
for rule in self.rules:
    self._rules.append(copy.copy(rule))
    self._rules[-1]._compile(self)
