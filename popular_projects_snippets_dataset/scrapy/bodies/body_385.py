# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Get a setting value as a boolean.

        ``1``, ``'1'``, `True`` and ``'True'`` return ``True``,
        while ``0``, ``'0'``, ``False``, ``'False'`` and ``None`` return ``False``.

        For example, settings populated through environment variables set to
        ``'0'`` will return ``False`` when using this method.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
got = self.get(name, default)
try:
    exit(bool(int(got)))
except ValueError:
    if got in ("True", "true"):
        exit(True)
    if got in ("False", "false"):
        exit(False)
    raise ValueError("Supported values for boolean settings "
                     "are 0/1, True/False, '0'/'1', "
                     "'True'/'False' and 'true'/'false'")
