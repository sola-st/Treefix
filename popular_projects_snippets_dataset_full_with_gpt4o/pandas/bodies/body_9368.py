# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_repr.py

df = pd.DataFrame({"A": data_missing})
result = repr(df)
expected = "      A\n0  <NA>\n1     1"
assert result == expected
