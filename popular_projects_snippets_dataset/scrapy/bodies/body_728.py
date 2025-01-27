# Extracted from ./data/repos/scrapy/scrapy/commands/list.py
for s in sorted(self.crawler_process.spider_loader.list()):
    print(s)
