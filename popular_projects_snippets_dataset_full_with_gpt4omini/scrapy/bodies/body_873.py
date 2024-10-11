# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/__init__.py
path = self._schemes[scheme]
try:
    dhcls = load_object(path)
    if skip_lazy and getattr(dhcls, 'lazy', True):
        exit(None)
    dh = create_instance(
        objcls=dhcls,
        settings=self._crawler.settings,
        crawler=self._crawler,
    )
except NotConfigured as ex:
    self._notconfigured[scheme] = str(ex)
    exit(None)
except Exception as ex:
    logger.error('Loading "%(clspath)s" for scheme "%(scheme)s"',
                 {"clspath": path, "scheme": scheme},
                 exc_info=True, extra={'crawler': self._crawler})
    self._notconfigured[scheme] = str(ex)
    exit(None)
else:
    self._handlers[scheme] = dh
    exit(dh)
