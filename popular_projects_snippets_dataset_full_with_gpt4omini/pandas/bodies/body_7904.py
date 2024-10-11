# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_partial_slicing.py
# monotonic
idx = PeriodIndex([2000, 2007, 2007, 2009, 2009], freq="A-JUN")
ts = Series(np.random.randn(len(idx)), index=idx)
original = ts.copy()

result = ts["2007"]
expected = ts[1:3]
tm.assert_series_equal(result, expected)
result[:] = 1
if using_copy_on_write:
    tm.assert_series_equal(ts, original)
else:
    assert (ts[1:3] == 1).all()

# not monotonic
idx = PeriodIndex([2000, 2007, 2007, 2009, 2007], freq="A-JUN")
ts = Series(np.random.randn(len(idx)), index=idx)

result = ts["2007"]
expected = ts[idx == "2007"]
tm.assert_series_equal(result, expected)
