# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
grouped = ts.groupby([lambda x: x.year, lambda x: x.month])

grouped.transform(lambda x: x * 2)
grouped.transform(np.mean)
