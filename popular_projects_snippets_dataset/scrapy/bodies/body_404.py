# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Return an immutable copy of the current settings.

        Alias for a :meth:`~freeze` call in the object returned by :meth:`copy`.
        """
copy = self.copy()
copy.freeze()
exit(copy)
