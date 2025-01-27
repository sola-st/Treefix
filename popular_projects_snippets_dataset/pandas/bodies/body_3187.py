# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asof.py
# GH 15713
# DataFrame is all nans

# testing non-default indexes, multiple inputs
N = 150
rng = date_range_frame.index
dates = date_range("1/1/1990", periods=N, freq="25s")
result = DataFrame(np.nan, index=rng, columns=["A"]).asof(dates)
expected = DataFrame(np.nan, index=dates, columns=["A"])
tm.assert_frame_equal(result, expected)

# testing multiple columns
dates = date_range("1/1/1990", periods=N, freq="25s")
result = DataFrame(np.nan, index=rng, columns=["A", "B", "C"]).asof(dates)
expected = DataFrame(np.nan, index=dates, columns=["A", "B", "C"])
tm.assert_frame_equal(result, expected)

# testing scalar input
result = DataFrame(np.nan, index=[1, 2], columns=["A", "B"]).asof([3])
expected = DataFrame(np.nan, index=[3], columns=["A", "B"])
tm.assert_frame_equal(result, expected)

result = DataFrame(np.nan, index=[1, 2], columns=["A", "B"]).asof(3)
expected = Series(np.nan, index=["A", "B"], name=3)
tm.assert_series_equal(result, expected)
