# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
# frame
result = isna_f(df)
expected = df.apply(isna_f)
tm.assert_frame_equal(result, expected)
