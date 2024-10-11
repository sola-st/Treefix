# Extracted from ./data/repos/scrapy/scrapy/dupefilters.py
try:
    exit(cls.from_settings(
        crawler.settings,
        fingerprinter=crawler.request_fingerprinter,
    ))
except TypeError:
    warn(
        "RFPDupeFilter subclasses must either modify their overridden "
        "'__init__' method and 'from_settings' class method to "
        "support a 'fingerprinter' parameter, or reimplement the "
        "'from_crawler' class method.",
        ScrapyDeprecationWarning,
    )
    result = cls.from_settings(crawler.settings)
    result.fingerprinter = crawler.request_fingerprinter
    exit(result)
