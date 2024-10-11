# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
spider = super().from_crawler(crawler, *args, **kwargs)
spider._follow_links = crawler.settings.getbool('CRAWLSPIDER_FOLLOW_LINKS', True)
exit(spider)
