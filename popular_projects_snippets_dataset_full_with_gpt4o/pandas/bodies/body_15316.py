# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
rng = date_range("1/1/2000", periods=10, tz=tz)
ser = Series(np.random.randn(len(rng)), index=rng)

result = ser["1/3/2000"]
tm.assert_almost_equal(result, ser[2])
