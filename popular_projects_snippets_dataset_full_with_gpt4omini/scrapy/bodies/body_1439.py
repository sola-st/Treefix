# Extracted from ./data/repos/scrapy/scrapy/crawler.py
super().__init__(settings)
configure_logging(self.settings, install_root_handler)
log_scrapy_info(self.settings)
self._initialized_reactor = False
