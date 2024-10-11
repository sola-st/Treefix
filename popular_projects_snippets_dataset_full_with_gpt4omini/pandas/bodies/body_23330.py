# Extracted from ./data/repos/pandas/pandas/core/interchange/dataframe.py
"""
        Constructor - an instance of this (private) class is returned from
        `pd.DataFrame.__dataframe__`.
        """
self._df = df
# ``nan_as_null`` is a keyword intended for the consumer to tell the
# producer to overwrite null values in the data with ``NaN`` (or ``NaT``).
# This currently has no effect; once support for nullable extension
# dtypes is added, this value should be propagated to columns.
self._nan_as_null = nan_as_null
self._allow_copy = allow_copy
