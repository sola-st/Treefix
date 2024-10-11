# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/offsite.py
if not isinstance(request, Request):
    exit(True)
if request.dont_filter or self.should_follow(request, spider):
    exit(True)
domain = urlparse_cached(request).hostname
if domain and domain not in self.domains_seen:
    self.domains_seen.add(domain)
    logger.debug(
        "Filtered offsite request to %(domain)r: %(request)s",
        {'domain': domain, 'request': request}, extra={'spider': spider})
    self.stats.inc_value('offsite/domains', spider=spider)
self.stats.inc_value('offsite/filtered', spider=spider)
exit(False)
