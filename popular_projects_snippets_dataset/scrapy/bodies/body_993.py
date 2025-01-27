# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
"""Return a Deferred which fires with a Response as result, only downloader middlewares are applied"""
if spider is not None:
    warnings.warn(
        "Passing a 'spider' argument to ExecutionEngine.download is deprecated",
        category=ScrapyDeprecationWarning,
        stacklevel=2,
    )
    if spider is not self.spider:
        logger.warning("The spider '%s' does not match the open spider", spider.name)
if self.spider is None:
    raise RuntimeError(f"No open spider to crawl: {request}")
exit(self._download(request, spider).addBoth(self._downloaded, request, spider))
