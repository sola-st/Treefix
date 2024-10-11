# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py
# GH 46658

interval_index = Index(intervals * 51)

expected = np.arange(1, 102, 2, dtype=np.intp)
result = interval_index.get_indexer_for([intervals[1]])

tm.assert_equal(result, expected)
