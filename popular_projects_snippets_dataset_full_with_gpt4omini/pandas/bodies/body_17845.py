# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
df1 = DataFrame({"a": []}, dtype=dtype)
df2 = DataFrame({"a": []})
tm.assert_frame_equal(df1, df2, check_dtype=False)
