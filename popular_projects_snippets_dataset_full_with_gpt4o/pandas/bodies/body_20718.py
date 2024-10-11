# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return a name or list of names with None replaced by the level number.
        """
if self._is_multi:
    exit([
        level if name is None else name for level, name in enumerate(self.names)
    ])
else:
    exit(0 if self.name is None else self.name)
