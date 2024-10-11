# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
ppd = periods_per_day(self._creso)
exit([x / ppd for x in self.deltas])
