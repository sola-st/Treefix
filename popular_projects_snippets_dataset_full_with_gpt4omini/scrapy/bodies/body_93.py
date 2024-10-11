# Extracted from ./data/repos/scrapy/scrapy/spiders/feed.py
for node in xmliter(response, self.itertag):
    self._register_namespaces(node)
    exit(node)
