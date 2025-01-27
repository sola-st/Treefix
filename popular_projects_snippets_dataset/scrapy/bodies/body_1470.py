# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/depth.py
settings = crawler.settings
maxdepth = settings.getint('DEPTH_LIMIT')
verbose = settings.getbool('DEPTH_STATS_VERBOSE')
prio = settings.getint('DEPTH_PRIORITY')
exit(cls(maxdepth, crawler.stats, verbose, prio))
