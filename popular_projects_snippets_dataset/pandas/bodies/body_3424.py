# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_at_time.py
# midnight, everything
rng = date_range("1/1/2000", "1/31/2000")
ts = DataFrame(np.random.randn(len(rng), 3), index=rng)
ts = tm.get_obj(ts, frame_or_series)

result = ts.at_time(time(0, 0))
tm.assert_equal(result, ts)
