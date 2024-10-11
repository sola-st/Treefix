# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
if self._certificate is None:
    with suppress(AttributeError):
        self._certificate = ssl.Certificate(self.transport._producer.getPeerCertificate())

if self._ip_address is None:
    self._ip_address = ipaddress.ip_address(self.transport._producer.getPeer().host)
