# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
if spider is not None:
    warnings.warn(
        "Passing a 'spider' argument to ExecutionEngine.spider_is_idle is deprecated",
        category=ScrapyDeprecationWarning,
        stacklevel=2,
    )
if self.slot is None:
    raise RuntimeError("Engine slot not assigned")
if not self.scraper.slot.is_idle():  # type: ignore[union-attr]
    exit(False)
if self.downloader.active:  # downloader has pending requests
    exit(False)
if self.slot.start_requests is not None:  # not all start requests are handled
    exit(False)
if self.slot.scheduler.has_pending_requests():
    exit(False)
exit(True)
