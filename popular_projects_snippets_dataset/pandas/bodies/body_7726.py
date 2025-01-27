# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_monotonic.py
i = MultiIndex.from_product([np.arange(10), np.arange(10)], names=["one", "two"])
assert i.is_monotonic_increasing is True
assert i._is_strictly_monotonic_increasing is True
assert Index(i.values).is_monotonic_increasing is True
assert i._is_strictly_monotonic_increasing is True

i = MultiIndex.from_product(
    [np.arange(10, 0, -1), np.arange(10)], names=["one", "two"]
)
assert i.is_monotonic_increasing is False
assert i._is_strictly_monotonic_increasing is False
assert Index(i.values).is_monotonic_increasing is False
assert Index(i.values)._is_strictly_monotonic_increasing is False

i = MultiIndex.from_product(
    [np.arange(10), np.arange(10, 0, -1)], names=["one", "two"]
)
assert i.is_monotonic_increasing is False
assert i._is_strictly_monotonic_increasing is False
assert Index(i.values).is_monotonic_increasing is False
assert Index(i.values)._is_strictly_monotonic_increasing is False

i = MultiIndex.from_product([[1.0, np.nan, 2.0], ["a", "b", "c"]])
assert i.is_monotonic_increasing is False
assert i._is_strictly_monotonic_increasing is False
assert Index(i.values).is_monotonic_increasing is False
assert Index(i.values)._is_strictly_monotonic_increasing is False

i = MultiIndex(
    levels=[["bar", "baz", "foo", "qux"], ["mom", "next", "zenith"]],
    codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]],
    names=["first", "second"],
)
assert i.is_monotonic_increasing is True
assert Index(i.values).is_monotonic_increasing is True
assert i._is_strictly_monotonic_increasing is True
assert Index(i.values)._is_strictly_monotonic_increasing is True

# mixed levels, hits the TypeError
i = MultiIndex(
    levels=[
        [1, 2, 3, 4],
        [
            "gb00b03mlx29",
            "lu0197800237",
            "nl0000289783",
            "nl0000289965",
            "nl0000301109",
        ],
    ],
    codes=[[0, 1, 1, 2, 2, 2, 3], [4, 2, 0, 0, 1, 3, -1]],
    names=["household_id", "asset_id"],
)

assert i.is_monotonic_increasing is False
assert i._is_strictly_monotonic_increasing is False

# empty
i = MultiIndex.from_arrays([[], []])
assert i.is_monotonic_increasing is True
assert Index(i.values).is_monotonic_increasing is True
assert i._is_strictly_monotonic_increasing is True
assert Index(i.values)._is_strictly_monotonic_increasing is True
