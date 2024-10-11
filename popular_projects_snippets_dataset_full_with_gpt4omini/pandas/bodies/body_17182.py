# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 4386
# pivot_table always returns a DataFrame
# when values is not list like and columns is None
# and aggfunc is not instance of list
df = DataFrame({"col1": [3, 4, 5], "col2": ["C", "D", "E"], "col3": [1, 3, 9]})

result = df.pivot_table("col1", index=["col3", "col2"], aggfunc=np.sum)
m = MultiIndex.from_arrays([[1, 3, 9], ["C", "D", "E"]], names=["col3", "col2"])
expected = DataFrame([3, 4, 5], index=m, columns=["col1"])

tm.assert_frame_equal(result, expected)

result = df.pivot_table("col1", index="col3", columns="col2", aggfunc=np.sum)
expected = DataFrame(
    [[3, np.NaN, np.NaN], [np.NaN, 4, np.NaN], [np.NaN, np.NaN, 5]],
    index=Index([1, 3, 9], name="col3"),
    columns=Index(["C", "D", "E"], name="col2"),
)

tm.assert_frame_equal(result, expected)

result = df.pivot_table("col1", index="col3", aggfunc=[np.sum])
m = MultiIndex.from_arrays([["sum"], ["col1"]])
expected = DataFrame([3, 4, 5], index=Index([1, 3, 9], name="col3"), columns=m)

tm.assert_frame_equal(result, expected)
