# Extracted from ./data/repos/scrapy/scrapy/core/downloader/contextfactory.py
super().__init__(*args, **kwargs)
self._ssl_method = method
self.tls_verbose_logging = tls_verbose_logging
if tls_ciphers:
    self.tls_ciphers = AcceptableCiphers.fromOpenSSLCipherString(tls_ciphers)
else:
    self.tls_ciphers = DEFAULT_CIPHERS
