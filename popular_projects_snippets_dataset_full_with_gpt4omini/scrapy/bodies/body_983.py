# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
"""
        Gracefully close the execution engine.
        If it has already been started, stop it. In all cases, close the spider and the downloader.
        """
if self.running:
    exit(self.stop())  # will also close spider and downloader
if self.spider is not None:
    exit(self.close_spider(self.spider, reason="shutdown"))  # will also close downloader
exit(succeed(self.downloader.close()))
