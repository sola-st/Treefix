# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unstack.py
# GH 19966
idx = MultiIndex.from_product(
    [["a", "b", "c"], [1, 2, 3]], names=[("A", "a"), ("B", "b")]
)
ser = Series(1, index=idx)
result = ser.unstack(("A", "a"))

expected = DataFrame(
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    columns=MultiIndex.from_tuples([("a",), ("b",), ("c",)], names=[("A", "a")]),
    index=pd.Index([1, 2, 3], name=("B", "b")),
)
tm.assert_frame_equal(result, expected)
