# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
idx1 = Index([1, 2, 3])
idx2 = Index([1, 2, 4])
kwargs = {"check_exact": check_exact, "rtol": rtol}

msg = """Index are different

Index values are different \\(33\\.33333 %\\)
\\[left\\]:  NumericIndex\\(\\[1, 2, 3\\], dtype='int64'\\)
\\[right\\]: NumericIndex\\(\\[1, 2, 4\\], dtype='int64'\\)"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_index_equal(idx1, idx2, **kwargs)
