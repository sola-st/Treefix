# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
rng = to_timedelta(np.arange(10), unit="s")

df = DataFrame({"time": rng})

result = concat([df, df])
tm.assert_frame_equal(result.iloc[:10], df)
tm.assert_frame_equal(result.iloc[10:], df)
