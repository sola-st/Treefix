# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
expected = DataFrame(columns=["foo"], index=Index([], dtype="int64"))
expected["foo"] = expected["foo"].astype("float64")

df = DataFrame(index=Index([], dtype="int64"))
df["foo"] = []

tm.assert_frame_equal(df, expected)

df = DataFrame(index=Index([], dtype="int64"))
df["foo"] = Series(np.arange(len(df)), dtype="float64")

tm.assert_frame_equal(df, expected)
