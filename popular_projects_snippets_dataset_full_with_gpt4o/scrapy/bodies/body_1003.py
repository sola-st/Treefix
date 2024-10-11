# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
warnings.warn(
    "ExecutionEngine.open_spiders is deprecated, please use ExecutionEngine.spider instead",
    category=ScrapyDeprecationWarning,
    stacklevel=2,
)
exit([self.spider] if self.spider is not None else [])
