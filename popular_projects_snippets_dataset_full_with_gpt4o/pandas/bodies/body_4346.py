# Extracted from ./data/repos/pandas/pandas/tests/frame/test_logical_ops.py
# GH#5808
df1a_int = DataFrame(1, index=[1], columns=["A"])
df1a_bool = DataFrame(True, index=[1], columns=["A"])

result = df1a_int | df1a_bool
tm.assert_frame_equal(result, df1a_bool)

# Check that this matches Series behavior
res_ser = df1a_int["A"] | df1a_bool["A"]
tm.assert_series_equal(res_ser, df1a_bool["A"])
