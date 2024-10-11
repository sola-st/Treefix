# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_asof.py
index = tm.makeDateIndex(100)

dt = index[0]
assert index.asof(dt) == dt
assert isna(index.asof(dt - timedelta(1)))

dt = index[-1]
assert index.asof(dt + timedelta(1)) == dt

dt = index[0].to_pydatetime()
assert isinstance(index.asof(dt), Timestamp)
