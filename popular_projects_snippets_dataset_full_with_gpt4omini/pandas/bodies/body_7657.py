# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_set.py
# https://github.com/pandas-dev/pandas/issues/41485
idx = MultiIndex.from_tuples(
    [
        (1, "one"),
        (3, "one"),
    ],
    names=["foo", "bar"],
)
with pytest.raises(TypeError, match="positional arguments"):
    idx.set_levels(["a", "b", "c"], 0)

with pytest.raises(TypeError, match="positional arguments"):
    idx.set_codes([[0, 1], [1, 0]], 0)
