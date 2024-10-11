# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
self.policy = policy or DefaultCookiePolicy()
self.jar = _CookieJar(self.policy)
self.jar._cookies_lock = _DummyLock()
self.check_expired_frequency = check_expired_frequency
self.processed = 0
