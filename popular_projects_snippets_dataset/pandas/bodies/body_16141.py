# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# GH#9680
tdi = pd.timedelta_range(start=0, periods=10, freq="1s")
ser = Series(np.random.normal(size=10), index=tdi)
assert "foo" not in ser.__dict__
msg = "'Series' object has no attribute 'foo'"
with pytest.raises(AttributeError, match=msg):
    ser.foo
