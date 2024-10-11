# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_join.py
#  GH-45661
multi_index = MultiIndex.from_product([interval_index, range_index])
result = multi_index.join(interval_index)

tm.assert_index_equal(result, multi_index)
