# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py

td = Timedelta(1)
td64 = td.to_timedelta64()

obj = constructor(td64, dtype=object)
assert isinstance(get1(obj), np.timedelta64)
