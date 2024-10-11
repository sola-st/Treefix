# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# test that having an all-NA column doesn't mess you up
df = df.copy()
df["bad"] = np.nan
agged = df.groupby(["A", "B"]).mean()

expected = df.groupby(["A", "B"]).mean()
expected["bad"] = np.nan

tm.assert_frame_equal(agged, expected)
