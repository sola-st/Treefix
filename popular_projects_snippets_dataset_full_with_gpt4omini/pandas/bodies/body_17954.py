# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
msg = """Index are different

Attribute "inferred_type" are different
\\[left\\]:  integer
\\[right\\]: floating"""

idx1 = Index([1, 2, 3])
idx2 = Index([1, 2, 3], dtype=np.float64)

with pytest.raises(AssertionError, match=msg):
    tm.assert_index_equal(idx1, idx2, exact=True, check_exact=check_exact)
