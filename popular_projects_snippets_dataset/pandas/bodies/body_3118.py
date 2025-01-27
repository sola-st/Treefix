# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#38434
ci = CategoricalIndex(["a", "b", "c"])
df = DataFrame(
    {"a": [1, 3], "b": [2, 4], "c": [5, 6]}, index=ci[:-1], columns=ci
)
result = df.shift(axis=1)

expected = DataFrame(
    {"a": [np.nan, np.nan], "b": [1, 3], "c": [2, 4]}, index=ci[:-1], columns=ci
)
tm.assert_frame_equal(result, expected)

# periods != 1
result = df.shift(2, axis=1)
expected = DataFrame(
    {"a": [np.nan, np.nan], "b": [np.nan, np.nan], "c": [1, 3]},
    index=ci[:-1],
    columns=ci,
)
tm.assert_frame_equal(result, expected)
