# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
values = np.arange(5).astype(np.int64).view("M8[s]")
if as_td:
    values = values - values[0]
    exit(TimedeltaArray._simple_new(values, dtype=values.dtype))
else:
    exit(DatetimeArray._simple_new(values, dtype=values.dtype))
