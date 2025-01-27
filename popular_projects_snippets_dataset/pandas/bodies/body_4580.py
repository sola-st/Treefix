# Extracted from ./data/repos/pandas/pandas/tests/test_multilevel.py
# GH 20888
group_keys = ["a", "b", "c"]
df = DataFrame({"a": [1], "b": [2], "c": [3], "d": [d]})

g = df[df.a == 2].groupby(group_keys)
result = g.first().index
expected = MultiIndex(
    levels=[[1], [2], [3]], codes=[[], [], []], names=["a", "b", "c"]
)

tm.assert_index_equal(result, expected)
