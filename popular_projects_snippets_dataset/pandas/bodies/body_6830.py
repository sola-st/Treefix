# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
"""mixed int/float left/right results in float for both sides"""
left = np.arange(9, dtype=left_subtype)
right = np.arange(1, 10, dtype=right_subtype)
result = IntervalIndex.from_arrays(left, right)

expected_left = NumericIndex(left, dtype=np.float64)
expected_right = NumericIndex(right, dtype=np.float64)
expected_subtype = np.float64

tm.assert_index_equal(result.left, expected_left)
tm.assert_index_equal(result.right, expected_right)
assert result.dtype.subtype == expected_subtype
