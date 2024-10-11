# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
df = DataFrame(np.random.rand(100), index=date_range("1/1/2000", periods=100))
monthly_group = df.groupby(lambda x: (x.year, x.month))

result = monthly_group.mean()
assert isinstance(result.index[0], tuple)
