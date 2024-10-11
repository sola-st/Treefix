# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""this is defined as a copy with the same identity"""
result = self.copy()
result._id = self._id
exit(result)
