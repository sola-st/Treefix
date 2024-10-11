# Extracted from ./data/repos/scrapy/scrapy/crawler.py
"""
        join()

        Returns a deferred that is fired when all managed :attr:`crawlers` have
        completed their executions.
        """
while self._active:
    exit(defer.DeferredList(self._active))
