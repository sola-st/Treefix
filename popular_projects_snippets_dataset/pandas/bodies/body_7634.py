# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_drop.py
index = idx[idx.get_loc("foo")]
dropped = index.droplevel(0)
assert dropped.name == "second"

index = MultiIndex(
    levels=[Index(range(4)), Index(range(4)), Index(range(4))],
    codes=[
        np.array([0, 0, 1, 2, 2, 2, 3, 3]),
        np.array([0, 1, 0, 0, 0, 1, 0, 1]),
        np.array([1, 0, 1, 1, 0, 0, 1, 0]),
    ],
    names=["one", "two", "three"],
)
dropped = index.droplevel(0)
assert dropped.names == ("two", "three")

dropped = index.droplevel("two")
expected = index.droplevel(1)
assert dropped.equals(expected)
