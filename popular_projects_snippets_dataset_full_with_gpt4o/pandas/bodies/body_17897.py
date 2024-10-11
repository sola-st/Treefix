# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_numpy_array_equal.py
a = np.array([np.nan], dtype=object)
b = np.array([pd.NA], dtype=object)

msg = """numpy array are different

numpy array values are different \\(100.0 %\\)
\\[left\\]:  \\[nan\\]
\\[right\\]: \\[<NA>\\]"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_numpy_array_equal(a, b)
