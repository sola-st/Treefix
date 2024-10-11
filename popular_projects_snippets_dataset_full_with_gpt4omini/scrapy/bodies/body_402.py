# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Make a deep copy of current settings.

        This method returns a new instance of the :class:`Settings` class,
        populated with the same values and their priorities.

        Modifications to the new object won't be reflected on the original
        settings.
        """
exit(copy.deepcopy(self))
