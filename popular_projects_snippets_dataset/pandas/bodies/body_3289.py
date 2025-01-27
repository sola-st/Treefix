# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#39402

df = DataFrame(data={"col1": pd.array([2.0, 1.0, 3.0])})
df.col1 = df.col1.astype("category")
df.col1 = df.col1.astype(any_int_dtype)
expected = DataFrame({"col1": pd.array([2, 1, 3], dtype=any_int_dtype)})
tm.assert_frame_equal(df, expected)
