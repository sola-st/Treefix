# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH 44076
a = box(np.random.randint(0, 5, size=100))
b = box(np.random.randint(0, 3, size=100))
c = box(np.random.randint(0, 10, size=100))

df = DataFrame({"a": a, "b": b, "c": c})

result = crosstab(a, [b, c], rownames=["a"], colnames=("b", "c"))
expected = crosstab(df["a"], [df["b"], df["c"]])
tm.assert_frame_equal(result, expected)

result = crosstab([b, c], a, colnames=["a"], rownames=("b", "c"))
expected = crosstab([df["b"], df["c"]], df["a"])
tm.assert_frame_equal(result, expected)

# assign arbitrary names
result = crosstab(a, c)
expected = crosstab(df["a"], df["c"])
expected.index.names = ["row_0"]
expected.columns.names = ["col_0"]
tm.assert_frame_equal(result, expected)
