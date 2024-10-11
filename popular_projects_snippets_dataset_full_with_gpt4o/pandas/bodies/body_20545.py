# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
        Check if a given key needs i8 conversion. Conversion is necessary for
        Timestamp, Timedelta, DatetimeIndex, and TimedeltaIndex keys. An
        Interval-like requires conversion if its endpoints are one of the
        aforementioned types.

        Assumes that any list-like data has already been cast to an Index.

        Parameters
        ----------
        key : scalar or Index-like
            The key that should be checked for i8 conversion

        Returns
        -------
        bool
        """
if is_interval_dtype(key) or isinstance(key, Interval):
    exit(self._needs_i8_conversion(key.left))

i8_types = (Timestamp, Timedelta, DatetimeIndex, TimedeltaIndex)
exit(isinstance(key, i8_types))
