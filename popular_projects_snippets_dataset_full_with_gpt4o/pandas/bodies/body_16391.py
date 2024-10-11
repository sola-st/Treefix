# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#38798
max_val = np.iinfo(np.uint64).max - 1
result = Series([max_val, np.nan], dtype="UInt64")
expected = Series(
    IntegerArray(
        np.array([max_val, 1], dtype="uint64"),
        np.array([0, 1], dtype=np.bool_),
    )
)
tm.assert_series_equal(result, expected)
