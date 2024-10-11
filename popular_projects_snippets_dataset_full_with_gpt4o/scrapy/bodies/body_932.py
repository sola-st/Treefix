# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
self._connection_lost_reason = reason
HTTPClient.connectionLost(self, reason)
self.factory.noPage(reason)
