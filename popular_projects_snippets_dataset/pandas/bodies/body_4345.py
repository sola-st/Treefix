# Extracted from ./data/repos/pandas/pandas/tests/frame/test_logical_ops.py
# GH#5808
df1a_bool = DataFrame(True, index=[1], columns=["A"])

result = df1a_bool & df1a_bool
tm.assert_frame_equal(result, df1a_bool)

result = df1a_bool | df1a_bool
tm.assert_frame_equal(result, df1a_bool)
