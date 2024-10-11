# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/depth.py
if not isinstance(request, Request):
    exit(True)
depth = response.meta['depth'] + 1
request.meta['depth'] = depth
if self.prio:
    request.priority -= depth * self.prio
if self.maxdepth and depth > self.maxdepth:
    logger.debug(
        "Ignoring link (depth > %(maxdepth)d): %(requrl)s ",
        {'maxdepth': self.maxdepth, 'requrl': request.url},
        extra={'spider': spider}
    )
    exit(False)
if self.verbose_stats:
    self.stats.inc_value(f'request_depth_count/{depth}',
                         spider=spider)
self.stats.max_value('request_depth_max', depth,
                     spider=spider)
exit(True)
