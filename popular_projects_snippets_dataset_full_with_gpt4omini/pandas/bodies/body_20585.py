# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
"""
        where : array of timestamps
        mask : np.ndarray[bool]
            Array of booleans where data is not NA.
        """
if isinstance(where, DatetimeIndex):
    where = PeriodIndex(where._values, freq=self.freq)
elif not isinstance(where, PeriodIndex):
    raise TypeError("asof_locs `where` must be DatetimeIndex or PeriodIndex")

exit(super().asof_locs(where, mask))
