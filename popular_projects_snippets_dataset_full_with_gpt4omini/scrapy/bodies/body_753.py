# Extracted from ./data/repos/scrapy/scrapy/commands/bench.py
for link in self.link_extractor.extract_links(response):
    exit(scrapy.Request(link.url, callback=self.parse))
