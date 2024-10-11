# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_repr.py

df = pd.DataFrame({"A": data_missing})
result = repr(df)
expected = "      A\n0  <NA>\n1   0.1"
assert result == expected
