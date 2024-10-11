# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx
result = idx / 1
expected = idx.astype("float64")
tm.assert_index_equal(result, expected)

result = idx / 2
expected = Index(idx.values / 2)
tm.assert_index_equal(result, expected)
