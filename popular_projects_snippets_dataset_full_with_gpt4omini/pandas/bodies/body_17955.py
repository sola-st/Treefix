# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
msg = """Index are different

Index classes are different
\\[left\\]:  NumericIndex\\(\\[1, 2, 3\\], dtype='int64'\\)
\\[right\\]: """

idx1 = Index([1, 2, 3])
idx2 = RangeIndex(range(3))

with pytest.raises(AssertionError, match=msg):
    tm.assert_index_equal(idx1, idx2, exact=True, check_exact=check_exact)
