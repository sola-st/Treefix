# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_almost_equal.py
# Empty compare.
_assert_almost_equal_both(
    np.array([], dtype=left_dtype),
    np.array([], dtype=right_dtype),
    check_dtype=False,
)
