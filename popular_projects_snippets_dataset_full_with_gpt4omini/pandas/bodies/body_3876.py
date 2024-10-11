# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
df = float_frame.copy()
df[:] = np.arange(np.prod(df.shape)).reshape(df.shape)

stacked = df.stack()
stacked_df = DataFrame({"foo": stacked, "bar": stacked})

unstacked = stacked.unstack()
unstacked_df = stacked_df.unstack()

tm.assert_frame_equal(unstacked, df)
tm.assert_frame_equal(unstacked_df["bar"], df)

unstacked_cols = stacked.unstack(0)
unstacked_cols_df = stacked_df.unstack(0)
tm.assert_frame_equal(unstacked_cols.T, df)
tm.assert_frame_equal(unstacked_cols_df["bar"].T, df)
