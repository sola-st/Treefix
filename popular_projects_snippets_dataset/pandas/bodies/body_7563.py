# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_analytics.py
# callable
index = idx

result = index.map(lambda x: x)
tm.assert_index_equal(result, index)
