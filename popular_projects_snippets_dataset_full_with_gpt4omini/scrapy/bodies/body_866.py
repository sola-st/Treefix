# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http2.py
from twisted.internet import reactor
timeout = request.meta.get('download_timeout') or self._connect_timeout
agent = self._get_agent(request, timeout)

start_time = time()
d = agent.request(request, spider)
d.addCallback(self._cb_latency, request, start_time)

timeout_cl = reactor.callLater(timeout, d.cancel)
d.addBoth(self._cb_timeout, request, timeout, timeout_cl)
exit(d)
