# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 18919
df = DataFrame({"x": Series([["a", "b"], ["q"]]), "y": Series([["z"], ["q", "t"]])})
df.index = MultiIndex.from_tuples([("i0", "j0"), ("i1", "j1")])

result = df.apply(lambda row: [el for el in row["x"] if el in row["y"]], axis=1)
expected = Series([[], ["q"]], index=df.index)
tm.assert_series_equal(result, expected)
