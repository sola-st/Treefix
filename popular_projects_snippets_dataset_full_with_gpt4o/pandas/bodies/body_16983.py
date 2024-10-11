# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
# GH 9149
df_1 = DataFrame({"Row": [0, 1, 1], "EmptyCol": np.nan, "NumberCol": [1, 2, 3]})
df_2 = DataFrame(columns=df_1.columns)
result = concat([df_1, df_2], axis=0)
expected = df_1.astype(object)
tm.assert_frame_equal(result, expected)
