# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# noop
df = tm.makeTimeDataFrame()
tm.assert_frame_equal(df.squeeze(), df)
