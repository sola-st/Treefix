# Extracted from ./data/repos/scrapy/scrapy/extensions/memusage.py
if self.warned:  # warn only once
    exit()
if self.get_virtual_size() > self.warning:
    self.crawler.stats.set_value('memusage/warning_reached', 1)
    mem = self.warning / 1024 / 1024
    logger.warning("Memory usage reached %(memusage)dMiB",
                   {'memusage': mem}, extra={'crawler': self.crawler})
    if self.notify_mails:
        subj = (
            f"{self.crawler.settings['BOT_NAME']} warning: "
            f"memory usage reached {mem}MiB at {socket.gethostname()}"
        )
        self._send_report(self.notify_mails, subj)
        self.crawler.stats.set_value('memusage/warning_notified', 1)
    self.warned = True
