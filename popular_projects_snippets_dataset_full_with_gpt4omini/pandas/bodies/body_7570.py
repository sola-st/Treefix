# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_conversion.py
# GH 22420
expected = ["z", 0, "a"]
mi = MultiIndex.from_arrays(
    [["a", "b", "c"], ["x", "y", "z"], ["q", "w", "e"]], names=expected
)
result = mi.to_frame().columns.tolist()
assert result == expected
