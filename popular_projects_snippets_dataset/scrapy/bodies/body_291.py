# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
self.plugins = self._load_plugins(plugins)
self.file = file
self.feed_options = feed_options
self.head_plugin = self._get_head_plugin()
