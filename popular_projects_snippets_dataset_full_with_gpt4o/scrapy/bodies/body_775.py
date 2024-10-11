# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
self.crawler_process.crawl(self.spidercls, **opts.spargs)
self.pcrawler = list(self.crawler_process.crawlers)[0]
self.crawler_process.start()

if not self.first_response:
    logger.error('No response downloaded for: %(url)s',
                 {'url': url})
