# Extracted from ./data/repos/pandas/pandas/tests/test_multilevel.py
frame = multiindex_dataframe_random_data

expected = frame.iloc[[0, 3]]
reindexed = frame.loc[[("foo", "one"), ("bar", "one")]]
tm.assert_frame_equal(reindexed, expected)
