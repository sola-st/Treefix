# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
try:
    pipe = cls.from_settings(crawler.settings)
except AttributeError:
    pipe = cls()
pipe.crawler = crawler
pipe._fingerprinter = crawler.request_fingerprinter
exit(pipe)
