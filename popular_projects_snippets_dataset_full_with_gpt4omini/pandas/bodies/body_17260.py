# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py
df = DataFrame(
    np.empty((3, 3)),
    index=MultiIndex.from_tuples([("A", x) for x in list("aBc")]),
    columns=MultiIndex.from_tuples([("C", x) for x in list("xyz")]),
)

level_names = ["L1", "L2"]

result = methodcaller(func, level_names)(df)
assert result.index.names == level_names
assert result.columns.names == [None, None]

result = methodcaller(func, level_names, axis=1)(df)
assert result.columns.names == ["L1", "L2"]
assert result.index.names == [None, None]
