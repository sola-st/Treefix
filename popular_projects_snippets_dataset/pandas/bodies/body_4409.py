# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
d = {
    ("a", "a"): {("i", "i"): 0, ("i", "j"): 1, ("j", "i"): 2},
    ("b", "a"): {("i", "i"): 6, ("i", "j"): 5, ("j", "i"): 4},
    ("b", "c"): {("i", "i"): 7, ("i", "j"): 8, ("j", "i"): 9},
}
_d = sorted(d.items())
df = DataFrame(d)
expected = DataFrame(
    [x[1] for x in _d], index=MultiIndex.from_tuples([x[0] for x in _d])
).T
expected.index = MultiIndex.from_tuples(expected.index)
tm.assert_frame_equal(
    df,
    expected,
)

d["z"] = {"y": 123.0, ("i", "i"): 111, ("i", "j"): 111, ("j", "i"): 111}
_d.insert(0, ("z", d["z"]))
expected = DataFrame(
    [x[1] for x in _d], index=Index([x[0] for x in _d], tupleize_cols=False)
).T
expected.index = Index(expected.index, tupleize_cols=False)
df = DataFrame(d)
df = df.reindex(columns=expected.columns, index=expected.index)
tm.assert_frame_equal(df, expected)
