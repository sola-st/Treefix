# Extracted from ./data/repos/scrapy/scrapy/commands/bench.py
with _BenchServer():
    self.crawler_process.crawl(_BenchSpider, total=100000)
    self.crawler_process.start()
