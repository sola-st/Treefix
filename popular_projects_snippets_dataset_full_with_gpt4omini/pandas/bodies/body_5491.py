# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
# GH#15183
ts = Timestamp("2011-01-03 00:00:00-0500", tz="US/Eastern")
other = Timestamp("2011-01-01 00:00:00-0500", tz="US/Eastern")
naive = Timestamp("2011-01-01 00:00:00")

arr = np.array([other, ts], dtype=object)
res = arr == ts
expected = np.array([False, True], dtype=bool)
assert (res == expected).all()

# 2D case
arr = np.array([[other, ts], [ts, other]], dtype=object)
res = arr != ts
expected = np.array([[True, False], [False, True]], dtype=bool)
assert res.shape == expected.shape
assert (res == expected).all()

# tzaware mismatch
arr = np.array([naive], dtype=object)
msg = "Cannot compare tz-naive and tz-aware timestamps"
with pytest.raises(TypeError, match=msg):
    arr < ts
