# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
df = DataFrame(
    [[1, 1, "x", "X"], [1, 1, "y", "Y"], [1, 2, "z", "Z"]], columns=list("ABCD")
)

df = df.set_index(["A", "B"])
mi = MultiIndex.from_tuples([(1, 1)])

df.loc[mi, "C"] = "_"

assert (df.xs((1, 1))["C"] == "_").all()
