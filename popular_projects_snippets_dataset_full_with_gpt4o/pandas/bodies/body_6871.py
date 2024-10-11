# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# 22866
index = index_flat

result = index.to_flat_index()
tm.assert_index_equal(result, index)
