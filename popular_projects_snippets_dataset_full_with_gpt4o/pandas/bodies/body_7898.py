# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_formats.py
df = pd.DataFrame({"A": [1, 2, 3]}, index=pd.date_range("2000", periods=3))
result = repr(df)
expected = "            A\n2000-01-01  1\n2000-01-02  2\n2000-01-03  3"
assert result == expected
