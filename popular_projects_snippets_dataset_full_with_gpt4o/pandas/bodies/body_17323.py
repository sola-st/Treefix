# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
df = tm.makeTimeDataFrame()
tm.assert_frame_equal(df.transpose().transpose(), df)
