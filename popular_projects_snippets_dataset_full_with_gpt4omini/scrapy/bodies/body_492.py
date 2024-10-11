# Extracted from ./data/repos/scrapy/scrapy/utils/log.py
from twisted.internet import reactor
logger.debug("Using reactor: %s.%s", reactor.__module__, reactor.__class__.__name__)
from twisted.internet import asyncioreactor
if isinstance(reactor, asyncioreactor.AsyncioSelectorReactor):
    logger.debug(
        "Using asyncio event loop: %s.%s",
        reactor._asyncioEventloop.__module__,
        reactor._asyncioEventloop.__class__.__name__,
    )
