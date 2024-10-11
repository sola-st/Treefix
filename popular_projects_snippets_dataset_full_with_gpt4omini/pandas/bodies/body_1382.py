# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#22036 setting with same-sized list
df = DataFrame([[0, "str", "str2"]], columns=["a", "b", "b"])

df.iloc[:, 2] = ["str3"]

expected = DataFrame([[0, "str", "str3"]], columns=["a", "b", "b"])
tm.assert_frame_equal(df, expected)
