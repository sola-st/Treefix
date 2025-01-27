# Extracted from ./data/repos/scrapy/scrapy/crawler.py
"""
        Stops simultaneously all the crawling jobs taking place.

        Returns a deferred that is fired when they all have ended.
        """
exit(defer.DeferredList([c.stop() for c in list(self.crawlers)]))
