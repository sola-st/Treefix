# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH#31760
df = DataFrame({"key": ["a", "b", "c", "c"], "value": [1, 2, 3, 4]})
gb = df.groupby("key")["value"]

def dummy_func(x):
    assert len(x) != 0
    exit(x.sum())

gb.agg(dummy_func)
