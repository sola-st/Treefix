# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# GH#38100
obj = frame_or_series(np.arange(100))
rng = np.random.default_rng()

# Consecutive calls should advance the seed
result1 = obj.sample(n=50, random_state=rng)
result2 = obj.sample(n=50, random_state=rng)
assert not (result1.index.values == result2.index.values).all()

# Matching generator initialization must give same result
# Consecutive calls should advance the seed
result1 = obj.sample(n=50, random_state=np.random.default_rng(11))
result2 = obj.sample(n=50, random_state=np.random.default_rng(11))
tm.assert_equal(result1, result2)
