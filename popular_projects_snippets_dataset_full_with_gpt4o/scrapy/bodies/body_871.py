# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/__init__.py
self._crawler = crawler
self._schemes = {}  # stores acceptable schemes on instancing
self._handlers = {}  # stores instanced handlers for schemes
self._notconfigured = {}  # remembers failed handlers
handlers = without_none_values(
    crawler.settings.getwithbase('DOWNLOAD_HANDLERS'))
for scheme, clspath in handlers.items():
    self._schemes[scheme] = clspath
    self._load_handler(scheme, skip_lazy=True)

crawler.signals.connect(self._close, signals.engine_stopped)
