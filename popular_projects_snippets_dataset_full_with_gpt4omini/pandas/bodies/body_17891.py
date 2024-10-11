# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_numpy_array_equal.py
msg = """Index are different

Index shapes are different
\\[left\\]:  \\(2L*,\\)
\\[right\\]: \\(3L*,\\)"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_numpy_array_equal(np.array([1, 2]), np.array([3, 4, 5]), obj="Index")
