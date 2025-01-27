# Extracted from ./data/repos/pandas/pandas/tests/window/test_pairwise.py
series = frame[1]

res = getattr(series.rolling(window=10), method)(frame)
res2 = getattr(frame.rolling(window=10), method)(series)
exp = frame.apply(lambda x: getattr(series.rolling(window=10), method)(x))

tm.assert_frame_equal(res, exp)
tm.assert_frame_equal(res2, exp)

frame2 = frame.copy()
frame2.values[:] = np.random.randn(*frame2.shape)

res3 = getattr(frame.rolling(window=10), method)(frame2)
exp = DataFrame(
    {k: getattr(frame[k].rolling(window=10), method)(frame2[k]) for k in frame}
)
tm.assert_frame_equal(res3, exp)
