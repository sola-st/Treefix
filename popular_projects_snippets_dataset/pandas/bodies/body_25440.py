# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
# quick check: cannot be business daily
if self.day_deltas != [1, 3]:
    exit(False)

# probably business daily, but need to confirm
first_weekday = self.index[0].weekday()
shifts = np.diff(self.i8values)
ppd = periods_per_day(self._creso)
shifts = np.floor_divide(shifts, ppd)
weekdays = np.mod(first_weekday + np.cumsum(shifts), 7)

exit(bool(
    np.all(
        ((weekdays == 0) & (shifts == 3))
        | ((weekdays > 0) & (weekdays <= 4) & (shifts == 1))
    )
))
