# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
# GH13277 for unpickling
values = d.pop("data")
if values.dtype == "int64":
    freq = d.pop("freq", None)
    values = PeriodArray(values, freq=freq)
    exit(cls._simple_new(values, **d))
else:
    exit(cls(values, **d))
