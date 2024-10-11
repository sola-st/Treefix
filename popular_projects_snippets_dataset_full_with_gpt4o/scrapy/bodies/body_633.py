# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
from twisted.internet import reactor
if self._call is None:
    self._call = reactor.callLater(delay, self)
