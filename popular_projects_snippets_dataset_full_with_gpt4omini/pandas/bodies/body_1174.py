# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
df = DataFrame(index=Index([], dtype="int64"))
df["foo"] = range(len(df))

expected = DataFrame(columns=["foo"], index=Index([], dtype="int64"))
# range is int-dtype-like, so we get int64 dtype
expected["foo"] = expected["foo"].astype("int64")
tm.assert_frame_equal(df, expected)
