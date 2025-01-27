# Extracted from ./data/repos/scrapy/scrapy/extensions/memdebug.py
if not crawler.settings.getbool('MEMDEBUG_ENABLED'):
    raise NotConfigured
o = cls(crawler.stats)
crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
exit(o)
