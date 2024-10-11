# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
result = index.astype("interval")
tm.assert_index_equal(result, index)

result = index.astype(index.dtype)
tm.assert_index_equal(result, index)
