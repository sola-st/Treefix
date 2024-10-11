# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
msg = """MultiIndex level \\[1\\] are different

MultiIndex level \\[1\\] values are different \\(25\\.0 %\\)
\\[left\\]:  NumericIndex\\(\\[2, 2, 3, 4\\], dtype='int64'\\)
\\[right\\]: NumericIndex\\(\\[1, 2, 3, 4\\], dtype='int64'\\)"""

idx1 = MultiIndex.from_tuples([("A", 2), ("A", 2), ("B", 3), ("B", 4)])
idx2 = MultiIndex.from_tuples([("A", 1), ("A", 2), ("B", 3), ("B", 4)])

with pytest.raises(AssertionError, match=msg):
    tm.assert_index_equal(idx1, idx2, check_exact=check_exact)
