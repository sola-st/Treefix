# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# Assigning a Category to parts of a int/... column uses the values of
# the Categorical
df = DataFrame({"a": [1, 1, 1, 1, 1], "b": list("aaaaa")})
exp = DataFrame({"a": [1, "b", "b", 1, 1], "b": list("aabba")})
df.loc[1:2, "a"] = Categorical(["b", "b"], categories=["a", "b"])
df.loc[2:3, "b"] = Categorical(["b", "b"], categories=["a", "b"])
tm.assert_frame_equal(df, exp)
