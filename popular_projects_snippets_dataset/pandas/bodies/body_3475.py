# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# see gh-10174

# interpolation method other than default linear
df = DataFrame({"A": [1, 2, 3], "B": [2, 3, 4]}, index=[1, 2, 3])
result = df.quantile(0.5, axis=1, interpolation="nearest")
expected = Series([1, 2, 3], index=[1, 2, 3], name=0.5)
tm.assert_series_equal(result, expected)

# cross-check interpolation=nearest results in original dtype
exp = np.percentile(
    np.array([[1, 2, 3], [2, 3, 4]]),
    0.5,
    axis=0,
    **{np_percentile_argname: "nearest"},
)
expected = Series(exp, index=[1, 2, 3], name=0.5, dtype="int64")
tm.assert_series_equal(result, expected)

# float
df = DataFrame({"A": [1.0, 2.0, 3.0], "B": [2.0, 3.0, 4.0]}, index=[1, 2, 3])
result = df.quantile(0.5, axis=1, interpolation="nearest")
expected = Series([1.0, 2.0, 3.0], index=[1, 2, 3], name=0.5)
tm.assert_series_equal(result, expected)
exp = np.percentile(
    np.array([[1.0, 2.0, 3.0], [2.0, 3.0, 4.0]]),
    0.5,
    axis=0,
    **{np_percentile_argname: "nearest"},
)
expected = Series(exp, index=[1, 2, 3], name=0.5, dtype="float64")
tm.assert_series_equal(result, expected)

# axis
result = df.quantile([0.5, 0.75], axis=1, interpolation="lower")
expected = DataFrame(
    {1: [1.0, 1.0], 2: [2.0, 2.0], 3: [3.0, 3.0]}, index=[0.5, 0.75]
)
tm.assert_frame_equal(result, expected)

# test degenerate case
df = DataFrame({"x": [], "y": []})
q = df.quantile(0.1, axis=0, interpolation="higher")
assert np.isnan(q["x"]) and np.isnan(q["y"])

# multi
df = DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 3]], columns=["a", "b", "c"])
result = df.quantile([0.25, 0.5], interpolation="midpoint")

# https://github.com/numpy/numpy/issues/7163
expected = DataFrame(
    [[1.5, 1.5, 1.5], [2.0, 2.0, 2.0]],
    index=[0.25, 0.5],
    columns=["a", "b", "c"],
)
tm.assert_frame_equal(result, expected)
