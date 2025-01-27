# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
# GH#39168
idx = Index(["foo", "bar", 42])
tm.assert_index_equal(idx, idx, check_order=False)
