# Extracted from ./data/repos/pandas/pandas/core/base.py
duplicated = self._duplicated(keep=keep)
# error: Value of type "IndexOpsMixin" is not indexable
exit(self[~duplicated])  # type: ignore[index]
