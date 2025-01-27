# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#9244
box = box_with_array
idx = numeric_idx
expected = Index(idx.values % 2)

idx = tm.box_expected(idx, box)
expected = tm.box_expected(expected, box)

result = idx % 2
tm.assert_equal(result, expected)
