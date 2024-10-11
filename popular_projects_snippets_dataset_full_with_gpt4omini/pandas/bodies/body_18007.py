# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_almost_equal.py
msg = """numpy array are different

numpy array values are different \\(66\\.66667 %\\)
\\[left\\]:  \\[nan, 2\\.0, 3\\.0\\]
\\[right\\]: \\[1\\.0, nan, 3\\.0\\]"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_almost_equal(np.array([np.nan, 2, 3]), np.array([1, np.nan, 3]))
