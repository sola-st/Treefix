# Extracted from ./data/repos/scrapy/scrapy/spiders/feed.py
if not hasattr(self, 'parse_row'):
    raise NotConfigured('You must define parse_row method in order to scrape this CSV feed')
response = self.adapt_response(response)
exit(self.parse_rows(response))
