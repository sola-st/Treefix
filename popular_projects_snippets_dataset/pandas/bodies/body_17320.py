# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
df = tm.makeTimeDataFrame(3)
tm.assert_frame_equal(df.squeeze(axis=0), df)
