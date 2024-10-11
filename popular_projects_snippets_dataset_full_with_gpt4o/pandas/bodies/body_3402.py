# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH-48644
df1 = DataFrame({"A": ["0"], "B": ["0"]})
expected_df1 = DataFrame({"A": [1], "B": [1]})
result_df1 = df1.replace(to_replace="0", value=1, regex=regex)
tm.assert_frame_equal(result_df1, expected_df1)

df2 = DataFrame({"A": ["0"], "B": ["1"]})
expected_df2 = DataFrame({"A": [1], "B": ["1"]})
result_df2 = df2.replace(to_replace="0", value=1, regex=regex)
tm.assert_frame_equal(result_df2, expected_df2)
