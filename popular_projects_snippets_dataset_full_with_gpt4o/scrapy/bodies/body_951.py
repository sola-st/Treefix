# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
exit((
    f"<downloader.Slot concurrency={self.concurrency!r} "
    f"delay={self.delay:.2f} randomize_delay={self.randomize_delay!r} "
    f"len(active)={len(self.active)} len(queue)={len(self.queue)} "
    f"len(transferring)={len(self.transferring)} "
    f"lastseen={datetime.fromtimestamp(self.lastseen).isoformat()}>"
))
