# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# result_type should be consistent no matter which
# path we take in the code
df = int_frame_const_col

result = df.apply(lambda x: [1, 2, 3], axis=1, result_type="expand")
expected = df.copy()
expected.columns = [0, 1, 2]
tm.assert_frame_equal(result, expected)
