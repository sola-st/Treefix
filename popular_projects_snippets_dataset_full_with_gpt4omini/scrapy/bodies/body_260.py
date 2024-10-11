# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
exporter = cls(crawler)
crawler.signals.connect(exporter.open_spider, signals.spider_opened)
crawler.signals.connect(exporter.close_spider, signals.spider_closed)
crawler.signals.connect(exporter.item_scraped, signals.item_scraped)
exit(exporter)
