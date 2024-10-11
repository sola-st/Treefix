# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_almost_equal.py
a = np.array([Timestamp("2011-01-01"), Timestamp("2011-01-01")])
b = np.array([Timestamp("2011-01-01"), Timestamp("2011-01-02")])

msg = """numpy array are different

numpy array values are different \\(50\\.0 %\\)
\\[left\\]:  \\[2011-01-01 00:00:00, 2011-01-01 00:00:00\\]
\\[right\\]: \\[2011-01-01 00:00:00, 2011-01-02 00:00:00\\]"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_almost_equal(a, b)
