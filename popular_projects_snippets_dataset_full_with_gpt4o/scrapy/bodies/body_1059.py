# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
"""
        Return the total amount of enqueued requests
        """
exit(len(self.dqs) + len(self.mqs) if self.dqs is not None else len(self.mqs))
