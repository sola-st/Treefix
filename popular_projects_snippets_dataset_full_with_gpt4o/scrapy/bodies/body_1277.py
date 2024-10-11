# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/robotstxt.py
if rp is None:
    exit()

useragent = self._robotstxt_useragent
if not useragent:
    useragent = request.headers.get(b'User-Agent', self._default_useragent)
if not rp.allowed(request.url, useragent):
    logger.debug("Forbidden by robots.txt: %(request)s",
                 {'request': request}, extra={'spider': spider})
    self.crawler.stats.inc_value('robotstxt/forbidden')
    raise IgnoreRequest("Forbidden by robots.txt")
