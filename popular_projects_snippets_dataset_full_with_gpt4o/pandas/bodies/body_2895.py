# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
# GH14687 - integer series that do no align exactly

df1 = DataFrame({"a": [0, 1, 3, 5]}, dtype="int64")
df2 = DataFrame({"a": [1, 4]}, dtype="int64")

result_12 = df1.combine_first(df2)
expected_12 = DataFrame({"a": [0, 1, 3, 5]})
tm.assert_frame_equal(result_12, expected_12)

result_21 = df2.combine_first(df1)
expected_21 = DataFrame({"a": [1, 4, 3, 5]})
tm.assert_frame_equal(result_21, expected_21)
