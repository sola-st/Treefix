# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#19843
df = DataFrame(index=range(3))
df["now"] = Timestamp("20130101", tz="UTC")

expected = DataFrame(
    [[Timestamp("20130101", tz="UTC")]] * 3, index=[0, 1, 2], columns=["now"]
)
tm.assert_frame_equal(df, expected)
