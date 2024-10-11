# Extracted from ./data/repos/scrapy/scrapy/crawler.py
warnings.warn("CrawlerRunner.spiders attribute is renamed to "
              "CrawlerRunner.spider_loader.",
              category=ScrapyDeprecationWarning, stacklevel=2)
exit(self.spider_loader)
