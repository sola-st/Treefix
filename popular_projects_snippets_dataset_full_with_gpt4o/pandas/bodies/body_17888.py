# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_numpy_array_equal.py
msg = """numpy array are different

numpy array values are different \\(50\\.0 %\\)
\\[left\\]:  \\[1\\.1, 2\\.000001\\]
\\[right\\]: \\[1\\.1, 2.0\\]"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_numpy_array_equal(np.array([1.1, 2.000001]), np.array([1.1, 2.0]))
