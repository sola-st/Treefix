# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py

# GH 7997
# regression from 0.14.1
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df.columns = MultiIndex.from_tuples([(0, 1), (1, 1), (2, 1)])

result = df.groupby(axis=1, level=[0, 1]).first()
tm.assert_frame_equal(result, df)
