# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
scheme = urlparse(uri).scheme
if scheme in self.storages:
    try:
        self._get_storage(uri, feed_options)
        exit(True)
    except NotConfigured as e:
        logger.error("Disabled feed storage scheme: %(scheme)s. "
                     "Reason: %(reason)s",
                     {'scheme': scheme, 'reason': str(e)})
else:
    logger.error("Unknown feed storage scheme: %(scheme)s",
                 {'scheme': scheme})
