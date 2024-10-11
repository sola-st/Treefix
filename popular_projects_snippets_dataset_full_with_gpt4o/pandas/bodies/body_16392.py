# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#38798
result = Series([np.nan, np.nan], dtype="UInt64")
expected = Series(
    IntegerArray(
        np.array([1, 1], dtype="uint64"),
        np.array([1, 1], dtype=np.bool_),
    )
)
tm.assert_series_equal(result, expected)
