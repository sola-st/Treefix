# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unstack.py
# GH#48763
arrays = [["a", "a"], [1, 2], ["red", "blue"]]
idx = MultiIndex.from_arrays(arrays, names=("x", 0, "y"))
ser = Series([1, 2], index=idx)
result = ser.unstack("x")
expected = DataFrame(
    [[1], [2]],
    columns=pd.Index(["a"], name="x"),
    index=MultiIndex.from_tuples([(1, "red"), (2, "blue")], names=[0, "y"]),
)
tm.assert_frame_equal(result, expected)
