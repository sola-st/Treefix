# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# regression
result = Series([1.0 * x for x in list(range(1, 10)) * 10])

data = np.random.random(1100) * 10.0
groupings = Series(data)

grouped = result.groupby(groupings)
grouped.mean()
