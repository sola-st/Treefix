# Extracted from ./data/repos/scrapy/scrapy/extensions/spiderstate.py
jobdir = job_dir(crawler.settings)
if not jobdir:
    raise NotConfigured

obj = cls(jobdir)
crawler.signals.connect(obj.spider_closed, signal=signals.spider_closed)
crawler.signals.connect(obj.spider_opened, signal=signals.spider_opened)
exit(obj)
