# Extracted from ./data/repos/scrapy/scrapy/extensions/memusage.py
peak_mem_usage = self.get_virtual_size()
if peak_mem_usage > self.limit:
    self.crawler.stats.set_value('memusage/limit_reached', 1)
    mem = self.limit / 1024 / 1024
    logger.error("Memory usage exceeded %(memusage)dMiB. Shutting down Scrapy...",
                 {'memusage': mem}, extra={'crawler': self.crawler})
    if self.notify_mails:
        subj = (
            f"{self.crawler.settings['BOT_NAME']} terminated: "
            f"memory usage exceeded {mem}MiB at {socket.gethostname()}"
        )
        self._send_report(self.notify_mails, subj)
        self.crawler.stats.set_value('memusage/limit_notified', 1)

    if self.crawler.engine.spider is not None:
        self.crawler.engine.close_spider(self.crawler.engine.spider, 'memusage_exceeded')
    else:
        self.crawler.stop()
else:
    logger.info("Peak memory usage is %(virtualsize)dMiB", {'virtualsize': peak_mem_usage / 1024 / 1024})
