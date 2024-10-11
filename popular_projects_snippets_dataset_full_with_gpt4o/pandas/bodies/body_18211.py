# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx
idx = tm.box_expected(idx, box_with_array)

result = op(idx, 1)
tm.assert_equal(result, idx)
