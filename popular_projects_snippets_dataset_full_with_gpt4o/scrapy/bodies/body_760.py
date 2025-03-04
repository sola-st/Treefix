# Extracted from ./data/repos/scrapy/scrapy/commands/crawl.py
if len(args) < 1:
    raise UsageError()
elif len(args) > 1:
    raise UsageError("running 'scrapy crawl' with more than one spider is not supported")
spname = args[0]

crawl_defer = self.crawler_process.crawl(spname, **opts.spargs)

if getattr(crawl_defer, 'result', None) is not None and issubclass(crawl_defer.result.type, Exception):
    self.exitcode = 1
else:
    self.crawler_process.start()

    if (
        self.crawler_process.bootstrap_failed
        or hasattr(self.crawler_process, 'has_exception') and self.crawler_process.has_exception
    ):
        self.exitcode = 1
