# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
# GH#31884
msg = """\
Index are different

Attribute "inferred_type" are different
\\[left\\]:  mixed
\\[right\\]: datetime"""

idx1 = Index([NA, np.datetime64("nat")])
idx2 = Index([NA, NaT])
with pytest.raises(AssertionError, match=msg):
    tm.assert_index_equal(idx1, idx2)
