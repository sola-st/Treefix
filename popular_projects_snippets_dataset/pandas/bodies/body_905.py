# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# GH#22372 Note the multi-step construction is necessary to trigger
#  the original bug. pandas/issues/22372#issuecomment-413345309
df = DataFrame(index=[0])
df["x"] = 1
df["cost"] = 2

# accessing df["cost"] adds "cost" to the _item_cache
df["cost"]

# This loc[[0]] lookup used to call _consolidate_inplace at the
#  BlockManager level, which failed to clear the _item_cache
df.loc[[0]]

df.at[0, "x"] = 4
df.at[0, "cost"] = 789

expected = DataFrame({"x": [4], "cost": 789}, index=[0])
tm.assert_frame_equal(df, expected)

# And in particular, check that the _item_cache has updated correctly.
tm.assert_series_equal(df["cost"], expected["cost"])
