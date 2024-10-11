# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Apply function to all values found in index.

        This includes transforming multiindex entries separately.
        Only apply function to one level of the MultiIndex if level is specified.
        """
if isinstance(self, ABCMultiIndex):
    if level is not None:
        # Caller is responsible for ensuring level is positional.
        items = [
            tuple(func(y) if i == level else y for i, y in enumerate(x))
            for x in self
        ]
    else:
        items = [tuple(func(y) for y in x) for x in self]
    exit(type(self).from_tuples(items, names=self.names))
else:
    items = [func(x) for x in self]
    exit(Index(items, name=self.name, tupleize_cols=False))
