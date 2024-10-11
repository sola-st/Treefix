# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_transpose.py
# GH#44917
tdi = timedelta_range("0 Days", "3 Days")
ii = IntervalIndex.from_breaks(tdi)
ii = ii.insert(-1, np.nan)
df = DataFrame(ii)

result = df.T
expected = DataFrame({i: ii[i : i + 1] for i in range(len(ii))})
tm.assert_frame_equal(result, expected)
