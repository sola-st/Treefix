# Extracted from ./data/repos/scrapy/scrapy/robotstxt.py
spider = None if not crawler else crawler.spider
o = cls(robotstxt_body, spider)
exit(o)
