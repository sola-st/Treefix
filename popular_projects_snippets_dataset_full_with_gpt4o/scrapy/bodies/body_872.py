# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/__init__.py
"""Lazy-load the downloadhandler for a scheme
        only on the first request for that scheme.
        """
if scheme in self._handlers:
    exit(self._handlers[scheme])
if scheme in self._notconfigured:
    exit(None)
if scheme not in self._schemes:
    self._notconfigured[scheme] = 'no handler available for that scheme'
    exit(None)

exit(self._load_handler(scheme))
