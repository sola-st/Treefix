# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_arithmetic.py

df = pd.DataFrame(
    {
        "A": pd.array([1, 2, np.nan], dtype="Float64"),
        "B": pd.array([1, np.nan, 3], dtype="Float32"),
        "C": np.array([1, 2, 3], dtype="float64"),
    }
)

result = df.A + df.C
expected = pd.Series([2, 4, np.nan], dtype="Float64")
tm.assert_series_equal(result, expected)

result = (df.A + df.C) * 3 == 12
expected = pd.Series([False, True, None], dtype="boolean")
tm.assert_series_equal(result, expected)

result = df.A + df.B
expected = pd.Series([2, np.nan, np.nan], dtype="Float64")
tm.assert_series_equal(result, expected)
