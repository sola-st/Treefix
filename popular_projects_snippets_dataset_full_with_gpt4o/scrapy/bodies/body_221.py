# Extracted from ./data/repos/scrapy/scrapy/extensions/closespider.py
from twisted.internet import reactor
self.task = reactor.callLater(self.close_on['timeout'],
                              self.crawler.engine.close_spider, spider,
                              reason='closespider_timeout')
