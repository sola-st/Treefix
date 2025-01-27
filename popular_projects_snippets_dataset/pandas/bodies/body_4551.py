# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
ts = fixed_now_ts + Timedelta(1)

obj = constructor(ts, dtype="M8[ns]")
assert get1(obj) == ts
