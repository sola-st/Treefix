# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
df = DataFrame(
    {"col1": [2, 5.0, 123, None], "col2": [1, 2, 3, 4]}, dtype=object
)

# since filling converts dtypes from object, changed expected to be
# object
filled = df.fillna(np.nan)
result = op(df, 3)
expected = op(filled, 3).astype(object)
expected[com.isna(expected)] = None
tm.assert_frame_equal(result, expected)

result = op(df, df)
expected = op(filled, filled).astype(object)
expected[com.isna(expected)] = None
tm.assert_frame_equal(result, expected)

result = op(df, df.fillna(7))
tm.assert_frame_equal(result, expected)

result = op(df.fillna(7), df)
tm.assert_frame_equal(result, expected, check_dtype=False)
