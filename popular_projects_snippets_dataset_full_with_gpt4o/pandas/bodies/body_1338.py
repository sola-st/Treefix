# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# Same as the "assign back to self" check in test_iloc_setitem_dups
#  but on a DataFrame with multiple blocks
df = DataFrame([[0, 1], [2, 3]], columns=["B", "B"])

# setting float values that can be held by existing integer arrays
#  is inplace
df.iloc[:, 0] = df.iloc[:, 0].astype("f8")
if not using_array_manager:
    assert len(df._mgr.blocks) == 1

# if the assigned values cannot be held by existing integer arrays,
#  we cast
df.iloc[:, 0] = df.iloc[:, 0] + 0.5
if not using_array_manager:
    assert len(df._mgr.blocks) == 2

expected = df.copy()

# assign back to self
df.iloc[[0, 1], [0, 1]] = df.iloc[[0, 1], [0, 1]]

tm.assert_frame_equal(df, expected)
