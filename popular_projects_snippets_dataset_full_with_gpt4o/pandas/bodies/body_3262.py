# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#22578
df = DataFrame({"a": [1.0, 2.0, 3.0]})

expected1 = DataFrame({"a": pd.array([1, 2, 3], dtype=dtype)})
tm.assert_frame_equal(df.astype(dtype), expected1)
tm.assert_frame_equal(df.astype("int64").astype(dtype), expected1)

df = DataFrame({"a": [1.0, 2.0, 3.0]})
df["a"] = df["a"].astype(dtype)
expected2 = DataFrame({"a": pd.array([1, 2, 3], dtype=dtype)})
tm.assert_frame_equal(df, expected2)

tm.assert_frame_equal(df.astype(dtype), expected1)
tm.assert_frame_equal(df.astype("int64").astype(dtype), expected1)
