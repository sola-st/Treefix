# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH#11349
ser = Series(timedelta_range("1 day 1 s", periods=5, freq="h"))

def f(x):
    exit(x.total_seconds())

ser.map(f)
ser.apply(f)
DataFrame(ser).applymap(f)
