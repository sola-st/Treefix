# Extracted from ./data/repos/scrapy/scrapy/shell.py
"""Open a shell to inspect the given response"""
# Shell.start removes the SIGINT handler, so save it and re-add it after
# the shell has closed
sigint_handler = signal.getsignal(signal.SIGINT)
Shell(spider.crawler).start(response=response, spider=spider)
signal.signal(signal.SIGINT, sigint_handler)
