# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_arithmetic.py

df = pd.DataFrame(
    {
        "A": pd.Series([1, 2, np.nan], dtype="Int64"),
        "B": pd.Series([1, np.nan, 3], dtype="UInt8"),
        "C": [1, 2, 3],
    }
)

result = df.A + df.C
expected = pd.Series([2, 4, np.nan], dtype="Int64")
tm.assert_series_equal(result, expected)

result = (df.A + df.C) * 3 == 12
expected = pd.Series([False, True, None], dtype="boolean")
tm.assert_series_equal(result, expected)

result = df.A + df.B
expected = pd.Series([2, np.nan, np.nan], dtype="Int64")
tm.assert_series_equal(result, expected)
