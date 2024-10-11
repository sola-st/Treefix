# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
"""Inject the request into the spider <-> downloader pipeline"""
if spider is not None:
    warnings.warn(
        "Passing a 'spider' argument to ExecutionEngine.crawl is deprecated",
        category=ScrapyDeprecationWarning,
        stacklevel=2,
    )
    if spider is not self.spider:
        raise RuntimeError(f"The spider {spider.name!r} does not match the open spider")
if self.spider is None:
    raise RuntimeError(f"No open spider to crawl: {request}")
self._schedule_request(request, self.spider)
self.slot.nextcall.schedule()  # type: ignore[union-attr]
