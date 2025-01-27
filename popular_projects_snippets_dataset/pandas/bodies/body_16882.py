# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# GH18914
df = DataFrame.from_dict({"GDP": [1, 2], "Nation": ["AB", "CD"]})
df = get_dummies(df, columns=["Nation"], sparse=sparse)
df2 = df.reindex(columns=["GDP"])

tm.assert_frame_equal(df[["GDP"]], df2)
