# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# corner, dtype=object
df1 = DataFrame({"col": ["foo", np.nan, "bar"]})
df2 = DataFrame({"col": ["foo", datetime.now(), "bar"]})
result = df1.ne(df2)
exp = DataFrame({"col": [False, True, False]})
tm.assert_frame_equal(result, exp)
