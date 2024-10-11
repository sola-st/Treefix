# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# result_type should be consistent no matter which
# path we take in the code
df = int_frame_const_col
# series result with other index
columns = ["other", "col", "names"]
result = df.apply(lambda x: Series([1, 2, 3], index=columns), axis=1)
expected = df.copy()
expected.columns = columns
tm.assert_frame_equal(result, expected)
