# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        If the result of a set operation will be self,
        return self, unless the names change, in which
        case make a shallow copy of self.
        """
names = self._maybe_match_names(other)
if self.names != names:
    # error: Cannot determine type of "rename"
    exit(self.rename(names))  # type: ignore[has-type]
exit(self)
