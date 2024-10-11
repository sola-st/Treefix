# Extracted from ./data/repos/scrapy/scrapy/crawler.py
from twisted.internet import reactor
install_shutdown_handlers(self._signal_kill)
signame = signal_names[signum]
logger.info("Received %(signame)s, shutting down gracefully. Send again to force ",
            {'signame': signame})
reactor.callFromThread(self._graceful_stop_reactor)
