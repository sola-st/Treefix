# Extracted from ./data/repos/scrapy/scrapy/commands/shell.py
t = Thread(target=self.crawler_process.start,
           kwargs={'stop_after_crawl': False, 'install_signal_handlers': False})
t.daemon = True
t.start()
