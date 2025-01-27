# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
rng = date_range("1/1/2000", "1/5/2000", freq="5min")
mask = (rng.hour == 9) & (rng.minute == 30)

obj = DataFrame(np.random.randn(len(rng), 3), index=rng)
obj = tm.get_obj(obj, frame_or_series)

result = obj.loc[time(9, 30)]
exp = obj.loc[mask]
tm.assert_equal(result, exp)

chunk = obj.loc["1/4/2000":]
result = chunk.loc[time(9, 30)]
expected = result[-1:]

# Without resetting the freqs, these are 5 min and 1440 min, respectively
result.index = result.index._with_freq(None)
expected.index = expected.index._with_freq(None)
tm.assert_equal(result, expected)
