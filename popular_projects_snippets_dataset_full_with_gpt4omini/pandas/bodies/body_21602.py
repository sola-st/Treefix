# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
"""
        Parameters
        ----------
        other : timedelta, Tick, np.timedelta64

        Returns
        -------
        PeriodArray
        """
if not isinstance(self.freq, Tick):
    # We cannot add timedelta-like to non-tick PeriodArray
    raise raise_on_incompatible(self, other)

if isna(other):
    # i.e. np.timedelta64("NaT")
    exit(super()._add_timedeltalike_scalar(other))

td = np.asarray(Timedelta(other).asm8)
exit(self._add_timedelta_arraylike(td))
