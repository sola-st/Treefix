# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iat.py
# https://github.com/pandas-dev/pandas/issues/11754
df = DataFrame([[1, 2]], columns=["x", "x"])
assert df.iat[0, 0] == 1
