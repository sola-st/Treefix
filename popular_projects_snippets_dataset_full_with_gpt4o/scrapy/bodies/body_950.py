# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
cls_name = self.__class__.__name__
exit((f"{cls_name}(concurrency={self.concurrency!r}, "
        f"delay={self.delay:.2f}, "
        f"randomize_delay={self.randomize_delay!r})"))
