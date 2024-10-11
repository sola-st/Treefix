# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# see gh-2793
df = DataFrame(
    {
        "a": np.array([1, 2, 3, 4], dtype=any_signed_int_numpy_dtype),
        "b": np.array([4.0, 3.0, 2.0, 1.0], dtype="float64"),
    }
)

expected = DataFrame(
    {"a": [np.nan, np.nan, 3.0, 4.0], "b": [4.0, 3.0, np.nan, np.nan]},
    dtype="float64",
)

result = df.where(df > 2, np.nan)
tm.assert_frame_equal(result, expected)

result = df.copy()
return_value = result.where(result > 2, np.nan, inplace=True)
assert return_value is None
tm.assert_frame_equal(result, expected)
