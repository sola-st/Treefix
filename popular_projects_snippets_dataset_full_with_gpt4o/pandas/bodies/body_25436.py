# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
ppd = periods_per_day(self._creso)
days = self.deltas[0] / ppd
if days % 7 == 0:
    # Weekly
    wd = int_to_weekday[self.rep_stamp.weekday()]
    alias = f"W-{wd}"
    exit(_maybe_add_count(alias, days / 7))
else:
    exit(_maybe_add_count("D", days))
