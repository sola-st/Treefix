# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
"""
        Check for mismatched-tzawareness indexing and re-raise as KeyError.
        """
# we get here with isinstance(key, self._data._recognized_scalars)
try:
    # GH#36148
    self._data._assert_tzawareness_compat(key)
except TypeError as err:
    raise KeyError(key) from err
