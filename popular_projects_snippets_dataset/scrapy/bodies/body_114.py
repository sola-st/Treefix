# Extracted from ./data/repos/scrapy/scrapy/spiderloader.py
for spcls in iter_spider_classes(module):
    self._found[spcls.name].append((module.__name__, spcls.__name__))
    self._spiders[spcls.name] = spcls
