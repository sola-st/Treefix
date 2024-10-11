# Extracted from ./data/repos/scrapy/scrapy/core/downloader/contextfactory.py
# setting verify=True will require you to provide CAs
# to verify against; in other words: it's not that simple

# backward-compatible SSL/TLS method:
#
# * this will respect `method` attribute in often recommended
#   `ScrapyClientContextFactory` subclass
#   (https://github.com/scrapy/scrapy/issues/1429#issuecomment-131782133)
#
# * getattr() for `_ssl_method` attribute for context factories
#   not calling super().__init__
exit(CertificateOptions(
    verify=False,
    method=getattr(self, 'method', getattr(self, '_ssl_method', None)),
    fixBrokenPeers=True,
    acceptableCiphers=self.tls_ciphers,
))
