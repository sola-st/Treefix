# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH#41570
df = DataFrame(
    {
        "a": pd.Series([1, 2], dtype="Int8"),
        "b": pd.Series([3, 4], dtype=dtype),
    }
)
result = df.melt()
expected = DataFrame(
    {
        "variable": ["a", "a", "b", "b"],
        "value": pd.Series([1, 2, 3, 4], dtype=dtype),
    }
)
tm.assert_frame_equal(result, expected)
