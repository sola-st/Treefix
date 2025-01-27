# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
"""Process each Request/Item (given in the output parameter) returned
        from the given spider
        """
assert self.slot is not None  # typing
if isinstance(output, Request):
    assert self.crawler.engine is not None  # typing
    self.crawler.engine.crawl(request=output)
elif is_item(output):
    self.slot.itemproc_size += 1
    dfd = self.itemproc.process_item(output, spider)
    dfd.addBoth(self._itemproc_finished, output, response, spider)
    exit(dfd)
elif output is None:
    pass
else:
    typename = type(output).__name__
    logger.error(
        'Spider must return request, item, or None, got %(typename)r in %(request)s',
        {'request': request, 'typename': typename},
        extra={'spider': spider},
    )
exit(None)
