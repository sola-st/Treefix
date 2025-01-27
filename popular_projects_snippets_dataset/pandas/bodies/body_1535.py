# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#16637
tdi = to_timedelta(range(10), unit="s")
df = DataFrame({"x": range(10)}, dtype="int64", index=tdi)

df.loc[df.index[indexer], "x"] = 20

expected = DataFrame(
    expected,
    index=tdi,
    columns=["x"],
    dtype="int64",
)

tm.assert_frame_equal(expected, df)
