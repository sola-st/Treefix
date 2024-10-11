# Extracted from ./data/repos/scrapy/scrapy/dupefilters.py
if self.debug:
    msg = "Filtered duplicate request: %(request)s (referer: %(referer)s)"
    args = {'request': request, 'referer': referer_str(request)}
    self.logger.debug(msg, args, extra={'spider': spider})
elif self.logdupes:
    msg = ("Filtered duplicate request: %(request)s"
           " - no more duplicates will be shown"
           " (see DUPEFILTER_DEBUG to show all duplicates)")
    self.logger.debug(msg, {'request': request}, extra={'spider': spider})
    self.logdupes = False

spider.crawler.stats.inc_value('dupefilter/filtered', spider=spider)
