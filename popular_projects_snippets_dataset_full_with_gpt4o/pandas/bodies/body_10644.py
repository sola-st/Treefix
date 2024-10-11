# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH#46995
df = DataFrame({"a": [1, 1, 2], "b": [3, 4, 5], "c": [6, 7, 8]})
gb = df.groupby("a", axis=1)
with pytest.raises(NotImplementedError, match="axis other than 0 is not supported"):
    gb.agg(func)
