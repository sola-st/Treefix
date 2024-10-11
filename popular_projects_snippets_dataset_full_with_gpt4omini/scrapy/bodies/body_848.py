# Extracted from ./data/repos/scrapy/scrapy/core/downloader/contextfactory.py
tls_verbose_logging = settings.getbool('DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING')
tls_ciphers = settings['DOWNLOADER_CLIENT_TLS_CIPHERS']
exit(cls(method=method, tls_verbose_logging=tls_verbose_logging, tls_ciphers=tls_ciphers, *args, **kwargs))
