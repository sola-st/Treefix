# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH#11314 with tz
index = date_range(
    datetime(2015, 10, 1), datetime(2015, 10, 1, 23), freq="H", tz="US/Eastern"
)
df = DataFrame(np.random.randn(24, 1), columns=["a"], index=index)
new_index = date_range(
    datetime(2015, 10, 2), datetime(2015, 10, 2, 23), freq="H", tz="US/Eastern"
)

result = df.set_index(new_index)
assert result.index.freq == index.freq
