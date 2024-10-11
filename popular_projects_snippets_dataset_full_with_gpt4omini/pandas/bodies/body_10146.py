# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
g = roll_frame.groupby("A", group_keys=False)
r = g.rolling(window=4)

result = r.quantile(0.4, interpolation=interpolation)
expected = g.apply(
    lambda x: x.rolling(4).quantile(0.4, interpolation=interpolation)
)
# groupby.apply doesn't drop the grouped-by column
expected = expected.drop("A", axis=1)
# GH 39732
expected_index = MultiIndex.from_arrays([roll_frame["A"], range(40)])
expected.index = expected_index
tm.assert_frame_equal(result, expected)
