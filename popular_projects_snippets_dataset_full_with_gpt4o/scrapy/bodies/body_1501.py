# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
self.default_policy = DefaultReferrerPolicy
if settings is not None:
    self.default_policy = _load_policy_class(
        settings.get('REFERRER_POLICY'))
