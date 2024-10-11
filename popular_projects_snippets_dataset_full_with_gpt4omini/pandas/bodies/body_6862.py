# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_join.py
#  GH-45661
flipped_interval_index = interval_index[::-1]
result = interval_index.join(flipped_interval_index)

tm.assert_index_equal(result, interval_index)
