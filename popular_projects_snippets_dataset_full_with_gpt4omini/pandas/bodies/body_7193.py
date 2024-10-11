# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
# https://github.com/pandas-dev/pandas/issues/35217
float_index = Index([1.0, 2, 3])
string_index = Index(["1", "2", "3"])

result = float_index.equals(string_index)
assert result is False

result = string_index.equals(float_index)
assert result is False
