# Extracted from ./data/repos/scrapy/scrapy/extensions/debug.py
self.crawler = crawler
try:
    signal.signal(signal.SIGUSR2, self.dump_stacktrace)
    signal.signal(signal.SIGQUIT, self.dump_stacktrace)
except AttributeError:
    # win32 platforms don't support SIGUSR signals
    pass
