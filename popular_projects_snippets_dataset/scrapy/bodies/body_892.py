# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
"""Asks the proxy to open a tunnel."""
tunnelReq = tunnel_request_data(self._tunneledHost, self._tunneledPort, self._proxyAuthHeader)
protocol.transport.write(tunnelReq)
self._protocolDataReceived = protocol.dataReceived
protocol.dataReceived = self.processProxyResponse
self._protocol = protocol
exit(protocol)
