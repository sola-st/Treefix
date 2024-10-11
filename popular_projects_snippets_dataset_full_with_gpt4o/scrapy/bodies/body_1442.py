# Extracted from ./data/repos/scrapy/scrapy/crawler.py
if isinstance(spidercls, str):
    spidercls = self.spider_loader.load(spidercls)
init_reactor = not self._initialized_reactor
self._initialized_reactor = True
exit(Crawler(spidercls, self.settings, init_reactor=init_reactor))
