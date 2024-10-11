# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
if not settings.getbool(self.enabled_setting):
    raise NotConfigured

self.max_redirect_times = settings.getint('REDIRECT_MAX_TIMES')
self.priority_adjust = settings.getint('REDIRECT_PRIORITY_ADJUST')
