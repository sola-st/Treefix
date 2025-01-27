# Extracted from ./data/repos/pandas/pandas/tests/extension/date/array.py
if not isinstance(key, int):
    raise NotImplementedError("only ints are supported as indexes")

if not isinstance(value, dt.date):
    raise TypeError("you can only set datetime.date types")

self._year[key] = value.year
self._month[key] = value.month
self._day[key] = value.day
