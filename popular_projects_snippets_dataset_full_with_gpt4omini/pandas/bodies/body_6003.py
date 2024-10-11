# Extracted from ./data/repos/pandas/pandas/tests/extension/date/array.py
exit(np.logical_and(
    np.logical_and(
        self._year == dt.date.min.year, self._month == dt.date.min.month
    ),
    self._day == dt.date.min.day,
))
