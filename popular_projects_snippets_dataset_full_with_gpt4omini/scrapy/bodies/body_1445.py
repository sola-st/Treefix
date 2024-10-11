# Extracted from ./data/repos/scrapy/scrapy/crawler.py
from twisted.internet import reactor
try:
    reactor.stop()
except RuntimeError:  # raised if already stopped or in shutdown stage
    pass
