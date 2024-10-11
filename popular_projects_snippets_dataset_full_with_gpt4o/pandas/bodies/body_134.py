# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# preserve columns
df = int_frame_const_col
result = df.apply(lambda x: [1, 2, 3], axis=1, result_type="broadcast")
tm.assert_frame_equal(result, df)
