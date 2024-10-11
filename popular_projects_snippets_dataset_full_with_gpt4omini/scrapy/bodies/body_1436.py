# Extracted from ./data/repos/scrapy/scrapy/crawler.py
if isinstance(spidercls, str):
    spidercls = self.spider_loader.load(spidercls)
exit(Crawler(spidercls, self.settings))
