# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
# check if using axes' names gives the same result
df = DataFrame([[2, 1], [4, 3]])
tm.assert_frame_equal(df.rank(axis=0), df.rank(axis="index"))
tm.assert_frame_equal(df.rank(axis=1), df.rank(axis="columns"))
