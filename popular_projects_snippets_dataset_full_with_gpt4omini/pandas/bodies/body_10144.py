# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
g = roll_frame.groupby("A", group_keys=False)
r = g.rolling(window=4)

result = getattr(r, f)()
expected = g.apply(lambda x: getattr(x.rolling(4), f)())
# groupby.apply doesn't drop the grouped-by column
expected = expected.drop("A", axis=1)
# GH 39732
expected_index = MultiIndex.from_arrays([roll_frame["A"], range(40)])
expected.index = expected_index
tm.assert_frame_equal(result, expected)
