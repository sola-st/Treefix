# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Similar to equals, but checks that object attributes and types are also equal.

        Returns
        -------
        bool
            If two Index objects have equal elements and same type True,
            otherwise False.
        """
exit((
    self.equals(other)
    and all(
        getattr(self, c, None) == getattr(other, c, None)
        for c in self._comparables
    )
    and type(self) == type(other)
))
