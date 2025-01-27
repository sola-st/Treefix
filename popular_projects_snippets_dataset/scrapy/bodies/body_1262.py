# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/cookies.py
if not crawler.settings.getbool('COOKIES_ENABLED'):
    raise NotConfigured
exit(cls(crawler.settings.getbool('COOKIES_DEBUG')))
