# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx

result = divmod(idx, 2)
with np.errstate(all="ignore"):
    div, mod = divmod(idx.values, 2)

expected = Index(div), Index(mod)
for r, e in zip(result, expected):
    tm.assert_index_equal(r, e)
