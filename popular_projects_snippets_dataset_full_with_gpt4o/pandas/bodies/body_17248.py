# Extracted from ./data/repos/pandas/pandas/tests/generic/test_series.py
ser = Series(
    [11, 21, 31],
    index=MultiIndex.from_tuples(
        [("A", x) for x in ["a", "B", "c"]], names=["l1", "l2"]
    ),
)

result = methodcaller(func, ["L1", "L2"])(ser)
assert ser.index.name is None
assert ser.index.names == ["l1", "l2"]
assert result.index.name is None
assert result.index.names, ["L1", "L2"]
