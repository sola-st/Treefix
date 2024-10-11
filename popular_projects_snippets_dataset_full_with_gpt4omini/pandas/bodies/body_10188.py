# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
g = frame.groupby("A", group_keys=False)
r = g.expanding()

result = getattr(r, f)()
expected = g.apply(lambda x: getattr(x.expanding(), f)())
# groupby.apply doesn't drop the grouped-by column
expected = expected.drop("A", axis=1)
# GH 39732
expected_index = MultiIndex.from_arrays([frame["A"], range(40)])
expected.index = expected_index
tm.assert_frame_equal(result, expected)
