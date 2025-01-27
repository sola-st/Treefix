# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_index.py
offset = cls(n=n)
rng = date_range(start="1/1/2000", periods=100000, freq="T")
ser = Series(rng)

res = rng + offset
assert res.freq is None  # not retained
assert res[0] == rng[0] + offset
assert res[-1] == rng[-1] + offset
res2 = ser + offset
# apply_index is only for indexes, not series, so no res2_v2
assert res2.iloc[0] == ser.iloc[0] + offset
assert res2.iloc[-1] == ser.iloc[-1] + offset
