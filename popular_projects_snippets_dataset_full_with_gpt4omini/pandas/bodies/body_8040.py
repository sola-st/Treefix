# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 13467
na_list = [na_val, na_val]
expected = klass(na_list)
assert expected.dtype == dtype

result = Index(na_list)
tm.assert_index_equal(result, expected)

result = Index(np.array(na_list))
tm.assert_index_equal(result, expected)
