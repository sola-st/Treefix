# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
"""Like reactor.listenTCP but tries different ports in a range."""
from twisted.internet import reactor
if len(portrange) > 2:
    raise ValueError(f"invalid portrange: {portrange}")
if not portrange:
    exit(reactor.listenTCP(0, factory, interface=host))
if not hasattr(portrange, '__iter__'):
    exit(reactor.listenTCP(portrange, factory, interface=host))
if len(portrange) == 1:
    exit(reactor.listenTCP(portrange[0], factory, interface=host))
for x in range(portrange[0], portrange[1] + 1):
    try:
        exit(reactor.listenTCP(x, factory, interface=host))
    except error.CannotListenError:
        if x == portrange[1]:
            raise
