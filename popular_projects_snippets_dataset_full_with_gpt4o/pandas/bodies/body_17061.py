# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
# GH 29879
df = DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
comb = concat([df, df], axis=axis, copy=True)
assert comb.index is not df.index
assert comb.columns is not df.columns
