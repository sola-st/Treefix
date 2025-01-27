# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# result_type should be consistent no matter which
# path we take in the code
df = int_frame_const_col
# broadcast result
result = df.apply(lambda x: [1, 2, 3], axis=1, result_type="broadcast")
expected = df.copy()
tm.assert_frame_equal(result, expected)
