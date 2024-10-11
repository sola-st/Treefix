# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_almost_equal.py
msg = """numpy array are different

numpy array values are different \\(50\\.0 %\\)
\\[left\\]:  \\[1, 2\\]
\\[right\\]: \\[1, 3\\]"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_almost_equal(np.array([1, 2]), np.array([1, 3]))
