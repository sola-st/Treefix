# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Store a key/value attribute with a given priority.

        Settings should be populated *before* configuring the Crawler object
        (through the :meth:`~scrapy.crawler.Crawler.configure` method),
        otherwise they won't have any effect.

        :param name: the setting name
        :type name: str

        :param value: the value to associate with the setting
        :type value: object

        :param priority: the priority of the setting. Should be a key of
            :attr:`~scrapy.settings.SETTINGS_PRIORITIES` or an integer
        :type priority: str or int
        """
self._assert_mutability()
priority = get_settings_priority(priority)
if name not in self:
    if isinstance(value, SettingsAttribute):
        self.attributes[name] = value
    else:
        self.attributes[name] = SettingsAttribute(value, priority)
else:
    self.attributes[name].set(value, priority)
