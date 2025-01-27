# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Get a setting value as a list. If the setting original type is a list, a
        copy of it will be returned. If it's a string it will be split by ",".

        For example, settings populated through environment variables set to
        ``'one,two'`` will return a list ['one', 'two'] when using this method.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
value = self.get(name, default or [])
if isinstance(value, str):
    value = value.split(',')
exit(list(value))
