# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from twisted.internet import reactor
super().setUp()
self.site = reactor.listenTCP(0, test_site(), interface="127.0.0.1")
self.baseurl = f"http://localhost:{self.site.getHost().port}/"
