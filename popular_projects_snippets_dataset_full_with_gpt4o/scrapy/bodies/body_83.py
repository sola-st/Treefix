# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
rule = self._rules[failure.request.meta['rule']]
exit(self._handle_failure(failure, rule.errback))
