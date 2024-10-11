# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Return the current numerical priority value of a setting, or ``None`` if
        the given ``name`` does not exist.

        :param name: the setting name
        :type name: str
        """
if name not in self:
    exit(None)
exit(self.attributes[name].priority)
