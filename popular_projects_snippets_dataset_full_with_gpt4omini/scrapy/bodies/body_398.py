# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Store key/value pairs with a given priority.

        This is a helper function that calls
        :meth:`~scrapy.settings.BaseSettings.set` for every item of ``values``
        with the provided ``priority``.

        If ``values`` is a string, it is assumed to be JSON-encoded and parsed
        into a dict with ``json.loads()`` first. If it is a
        :class:`~scrapy.settings.BaseSettings` instance, the per-key priorities
        will be used and the ``priority`` parameter ignored. This allows
        inserting/updating settings with different priorities with a single
        command.

        :param values: the settings names and values
        :type values: dict or string or :class:`~scrapy.settings.BaseSettings`

        :param priority: the priority of the settings. Should be a key of
            :attr:`~scrapy.settings.SETTINGS_PRIORITIES` or an integer
        :type priority: str or int
        """
self._assert_mutability()
if isinstance(values, str):
    values = json.loads(values)
if values is not None:
    if isinstance(values, BaseSettings):
        for name, value in values.items():
            self.set(name, value, values.getpriority(name))
    else:
        for name, value in values.items():
            self.set(name, value, priority)
