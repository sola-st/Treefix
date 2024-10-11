# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
pph = periods_per_day(self._creso) // 24
exit([x / pph for x in self.deltas])
