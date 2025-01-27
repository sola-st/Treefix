# Extracted from ./data/repos/scrapy/scrapy/core/downloader/contextfactory.py
ssl_method = openssl_methods[settings.get('DOWNLOADER_CLIENT_TLS_METHOD')]
context_factory_cls = load_object(settings['DOWNLOADER_CLIENTCONTEXTFACTORY'])
# try method-aware context factory
try:
    context_factory = create_instance(
        objcls=context_factory_cls,
        settings=settings,
        crawler=crawler,
        method=ssl_method,
    )
except TypeError:
    # use context factory defaults
    context_factory = create_instance(
        objcls=context_factory_cls,
        settings=settings,
        crawler=crawler,
    )
    msg = (
        f"{settings['DOWNLOADER_CLIENTCONTEXTFACTORY']} does not accept "
        "a `method` argument (type OpenSSL.SSL method, e.g. "
        "OpenSSL.SSL.SSLv23_METHOD) and/or a `tls_verbose_logging` "
        "argument and/or a `tls_ciphers` argument. Please, upgrade your "
        "context factory class to handle them or ignore them."
    )
    warnings.warn(msg)

exit(context_factory)
