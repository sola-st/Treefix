# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# https://github.com/pandas-dev/pandas/pull/43507#issuecomment-920375856
df1 = DataFrame({"a": [1], "b": [pd.Timestamp("2012-01-01")]})
df2 = DataFrame({"a": [2]})

result = concat([df1, df2.reindex(columns=df1.columns)], ignore_index=True)
expected = df1 = DataFrame({"a": [1, 2], "b": [pd.Timestamp("2012-01-01"), pd.NaT]})
tm.assert_frame_equal(result, expected)
