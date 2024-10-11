# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Get a setting value without affecting its original type.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
exit(self[name] if self[name] is not None else default)
