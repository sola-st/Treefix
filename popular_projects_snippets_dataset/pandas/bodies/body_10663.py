# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply_mutate.py

# GH 8467
# first show's mutation indicator
# second does not, but should yield the same results
df = pd.DataFrame({"key": [1, 1, 1, 2, 2, 2, 3, 3, 3], "value": range(9)})

result1 = df.groupby("key", group_keys=True).apply(lambda x: x[:].key)
result2 = df.groupby("key", group_keys=True).apply(lambda x: x.key)
tm.assert_series_equal(result1, result2)
