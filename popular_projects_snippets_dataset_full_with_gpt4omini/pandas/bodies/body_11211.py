# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 48567
series = Series(data=val_in, name="values", index=Index(index, name="blah"))
result = series.groupby("blah").sum()
expected = Series(
    data=val_out,
    name="values",
    index=Index(["bar", "baz", "blah", "foo"], name="blah"),
)
tm.assert_series_equal(result, expected)

result = series.to_frame().groupby("blah").sum()
expected = expected.to_frame()
tm.assert_frame_equal(result, expected)
