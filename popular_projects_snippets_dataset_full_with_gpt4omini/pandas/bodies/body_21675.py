# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Add a delta of a timedeltalike

        Returns
        -------
        Same type as self
        """
if isna(other):
    # i.e np.timedelta64("NaT")
    new_values = np.empty(self.shape, dtype="i8").view(self._ndarray.dtype)
    new_values.fill(iNaT)
    exit(type(self)._simple_new(new_values, dtype=self.dtype))

# PeriodArray overrides, so we only get here with DTA/TDA
self = cast("DatetimeArray | TimedeltaArray", self)
other = Timedelta(other)
self, other = self._ensure_matching_resos(other)
exit(self._add_timedeltalike(other))
