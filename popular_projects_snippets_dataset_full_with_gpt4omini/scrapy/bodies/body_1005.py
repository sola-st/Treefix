# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
warnings.warn(
    "ExecutionEngine.schedule is deprecated, please use "
    "ExecutionEngine.crawl or ExecutionEngine.download instead",
    category=ScrapyDeprecationWarning,
    stacklevel=2,
)
if self.slot is None:
    raise RuntimeError("Engine slot not assigned")
self._schedule_request(request, spider)
