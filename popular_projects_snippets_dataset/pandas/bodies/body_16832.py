# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
reindexed = [x.reindex(exp_index) for x in df_list]
expected = reindexed[0].join(reindexed[1:])
tm.assert_frame_equal(result, expected)
