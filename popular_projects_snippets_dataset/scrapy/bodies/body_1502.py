# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
if not crawler.settings.getbool('REFERER_ENABLED'):
    raise NotConfigured
mw = cls(crawler.settings)

# Note: this hook is a bit of a hack to intercept redirections
crawler.signals.connect(mw.request_scheduled, signal=signals.request_scheduled)

exit(mw)
