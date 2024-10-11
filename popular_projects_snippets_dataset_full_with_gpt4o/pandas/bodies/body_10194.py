# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
g = frame.groupby("A", group_keys=False)
r = g.expanding()

# reduction
result = r.apply(lambda x: x.sum(), raw=raw)
expected = g.apply(lambda x: x.expanding().apply(lambda y: y.sum(), raw=raw))
# groupby.apply doesn't drop the grouped-by column
expected = expected.drop("A", axis=1)
# GH 39732
expected_index = MultiIndex.from_arrays([frame["A"], range(40)])
expected.index = expected_index
tm.assert_frame_equal(result, expected)
