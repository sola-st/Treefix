# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
if not crawler.settings.getbool('DOWNLOADER_STATS'):
    raise NotConfigured
exit(cls(crawler.stats))
