# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcompression.py
if not crawler.settings.getbool('COMPRESSION_ENABLED'):
    raise NotConfigured
try:
    exit(cls(stats=crawler.stats))
except TypeError:
    warnings.warn(
        "HttpCompressionMiddleware subclasses must either modify "
        "their '__init__' method to support a 'stats' parameter or "
        "reimplement the 'from_crawler' method.",
        ScrapyDeprecationWarning,
    )
    result = cls()
    result.stats = crawler.stats
    exit(result)
