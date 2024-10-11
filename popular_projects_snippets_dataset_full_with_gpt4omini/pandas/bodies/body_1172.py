# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# these work as they don't really change
# anything but the index
# GH#5632
expected = DataFrame(columns=["foo"], index=Index([], dtype="object"))

df = DataFrame(index=Index([], dtype="object"))
df["foo"] = Series([], dtype="object")

tm.assert_frame_equal(df, expected)

df = DataFrame(index=Index([]))
df["foo"] = Series(df.index)

tm.assert_frame_equal(df, expected)

df = DataFrame(index=Index([]))
df["foo"] = df.index

tm.assert_frame_equal(df, expected)
