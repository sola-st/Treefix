# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
df = frame_for_truncated_bingrouper

# We need to create a GroupBy object with only one non-NaT group,
#  so use a huge freq so that all non-NaT dates will be grouped together
tdg = Grouper(key="Date", freq="100Y")
gb = df.groupby(tdg)

# check that we will go through the singular_series path
#  in _wrap_applied_output_series
assert gb.ngroups == 1
assert gb._selected_obj._get_axis(gb.axis).nlevels == 1

# function that returns a Series
res = gb.apply(lambda x: x["Quantity"] * 2)

expected = DataFrame(
    [[36, 6, 6, 10, 2]],
    index=Index([Timestamp("2013-12-31")], name="Date"),
    columns=Index([0, 1, 5, 2, 3], name="Quantity"),
)
tm.assert_frame_equal(res, expected)
