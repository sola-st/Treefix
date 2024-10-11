# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_head_tail.py
tm.assert_frame_equal(float_frame.head(), float_frame[:5])
tm.assert_frame_equal(float_frame.tail(), float_frame[-5:])

tm.assert_frame_equal(float_frame.head(0), float_frame[0:0])
tm.assert_frame_equal(float_frame.tail(0), float_frame[0:0])

tm.assert_frame_equal(float_frame.head(-1), float_frame[:-1])
tm.assert_frame_equal(float_frame.tail(-1), float_frame[1:])
tm.assert_frame_equal(float_frame.head(1), float_frame[:1])
tm.assert_frame_equal(float_frame.tail(1), float_frame[-1:])
# with a float index
df = float_frame.copy()
df.index = np.arange(len(float_frame)) + 0.1
tm.assert_frame_equal(df.head(), df.iloc[:5])
tm.assert_frame_equal(df.tail(), df.iloc[-5:])
tm.assert_frame_equal(df.head(0), df[0:0])
tm.assert_frame_equal(df.tail(0), df[0:0])
tm.assert_frame_equal(df.head(-1), df.iloc[:-1])
tm.assert_frame_equal(df.tail(-1), df.iloc[1:])
