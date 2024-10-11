# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame(float_frame)
tm.assert_frame_equal(df, float_frame)

df_casted = DataFrame(float_frame, dtype=np.int64)
assert df_casted.values.dtype == np.int64
