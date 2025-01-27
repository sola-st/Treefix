# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
self._assert_mutability()
priority = get_settings_priority(priority)
if priority >= self.getpriority(name):
    del self.attributes[name]
