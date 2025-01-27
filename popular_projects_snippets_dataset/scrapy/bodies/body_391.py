# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""Get a composition of a dictionary-like setting and its `_BASE`
        counterpart.

        :param name: name of the dictionary-like setting
        :type name: str
        """
compbs = BaseSettings()
compbs.update(self[name + '_BASE'])
compbs.update(self[name])
exit(compbs)
