# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
ser = Series(
    ["aBAD", np.nan, "bBAD", True, datetime.today(), "fooBAD", None, 1, 2.0]
)
result = Series(ser).str.replace("BAD[_]*", "", regex=True)
expected = Series(["a", np.nan, "b", np.nan, np.nan, "foo", np.nan, np.nan, np.nan])
tm.assert_series_equal(result, expected)
