# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx

result = idx * idx
tm.assert_index_equal(result, idx**2)
