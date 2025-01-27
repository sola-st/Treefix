# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_between_time.py
index = date_range("2012-01-01", "2012-01-05", freq="30min")
df = DataFrame(np.random.randn(len(index), 5), index=index)
bkey = slice(time(13, 0, 0), time(14, 0, 0))
binds = [26, 27, 28, 74, 75, 76, 122, 123, 124, 170, 171, 172]

result = df.between_time(bkey.start, bkey.stop)
expected = df.loc[bkey]
expected2 = df.iloc[binds]
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result, expected2)
assert len(result) == 12
