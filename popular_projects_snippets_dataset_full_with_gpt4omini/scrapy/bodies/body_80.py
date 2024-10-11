# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
exit(Request(
    url=link.url,
    callback=self._callback,
    errback=self._errback,
    meta=dict(rule=rule_index, link_text=link.text),
))
