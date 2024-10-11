# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/robotstxt.py
self.crawler.stats.inc_value('robotstxt/response_count')
self.crawler.stats.inc_value(f'robotstxt/response_status_count/{response.status}')
rp = self._parserimpl.from_crawler(self.crawler, response.body)
rp_dfd = self._parsers[netloc]
self._parsers[netloc] = rp
rp_dfd.callback(rp)
