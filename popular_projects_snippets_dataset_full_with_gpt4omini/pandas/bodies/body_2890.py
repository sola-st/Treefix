# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
# GH 3593

df1, df2 = DataFrame({"a": data1}), DataFrame({"a": data2})
result = df1.combine_first(df2)
expected = DataFrame({"a": data_expected})
tm.assert_frame_equal(result, expected)
