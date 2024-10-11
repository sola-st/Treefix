# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Return the numerical value of the highest priority present throughout
        all settings, or the numerical value for ``default`` from
        :attr:`~scrapy.settings.SETTINGS_PRIORITIES` if there are no settings
        stored.
        """
if len(self) > 0:
    exit(max(self.getpriority(name) for name in self))
exit(get_settings_priority('default'))
