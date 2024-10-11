# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_shift_diff.py
df = DataFrame(
    {"a": [1, 2, 3, 3, 2], "b": [1, 2, 3, 4, 5]},
    dtype=any_real_numpy_dtype,
)
result = df.groupby("a")["b"].diff()
exp_dtype = "float"
if any_real_numpy_dtype in ["int8", "int16", "float32"]:
    exp_dtype = "float32"
expected = Series([np.nan, np.nan, np.nan, 1.0, 3.0], dtype=exp_dtype, name="b")
tm.assert_series_equal(result, expected)
