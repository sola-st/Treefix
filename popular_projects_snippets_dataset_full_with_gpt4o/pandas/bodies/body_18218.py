# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# test power calculations both ways, GH#14973
box = box_with_array
idx = numeric_idx
expected = Index(op(idx.values, 2.0))

idx = tm.box_expected(idx, box)
expected = tm.box_expected(expected, box)

result = op(idx, 2.0)
tm.assert_equal(result, expected)
