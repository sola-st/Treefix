# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""Get a setting value as either a :class:`dict` or a :class:`list`.

        If the setting is already a dict or a list, a copy of it will be
        returned.

        If it is a string it will be evaluated as JSON, or as a comma-separated
        list of strings as a fallback.

        For example, settings populated from the command line will return:

        -   ``{'key1': 'value1', 'key2': 'value2'}`` if set to
            ``'{"key1": "value1", "key2": "value2"}'``

        -   ``['one', 'two']`` if set to ``'["one", "two"]'`` or ``'one,two'``

        :param name: the setting name
        :type name: string

        :param default: the value to return if no setting is found
        :type default: any
        """
value = self.get(name, default)
if value is None:
    exit({})
if isinstance(value, str):
    try:
        exit(json.loads(value))
    except ValueError:
        exit(value.split(','))
exit(copy.deepcopy(value))
