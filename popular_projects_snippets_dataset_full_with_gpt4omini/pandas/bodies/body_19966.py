# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        Require they keys to be the same type as the index. (so we don't
        fallback)
        """
# GH 26989
# For series, unpacking key needs to result in the label.
# This is already the case for len(key) == 1; e.g. (1,)
if self.ndim == 1 and len(key) > 1:
    key = (key,)

exit(key)
