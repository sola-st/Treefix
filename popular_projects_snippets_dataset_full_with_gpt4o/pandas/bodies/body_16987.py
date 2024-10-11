# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
# 39037
df1 = DataFrame(columns=["a", "b"])
df2 = DataFrame(columns=["b", "c"])
result = concat([df1, df2, df1])
expected = DataFrame(columns=["a", "b", "c"])
tm.assert_frame_equal(result, expected)

df3 = DataFrame(columns=["a", "b"])
df4 = DataFrame(columns=["b"])
result = concat([df3, df4])
expected = DataFrame(columns=["a", "b"])
tm.assert_frame_equal(result, expected)
