# Extracted from ./data/repos/scrapy/scrapy/crawler.py
"""Starts a graceful stop of the crawler and returns a deferred that is
        fired when the crawler is stopped."""
if self.crawling:
    self.crawling = False
    exit(defer.maybeDeferred(self.engine.stop))
