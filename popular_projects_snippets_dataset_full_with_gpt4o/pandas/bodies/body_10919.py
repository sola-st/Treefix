# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nunique.py
df = DataFrame({"A": list("abbacc"), "B": list("abxacc"), "C": list("abbacx")})

expected = DataFrame({"A": list("abc"), "B": [1, 2, 1], "C": [1, 1, 2]})
result = df.groupby("A", as_index=False).nunique()
tm.assert_frame_equal(result, expected)

# as_index
expected.index = list("abc")
expected.index.name = "A"
expected = expected.drop(columns="A")
result = df.groupby("A").nunique()
tm.assert_frame_equal(result, expected)

# with na
result = df.replace({"x": None}).groupby("A").nunique(dropna=False)
tm.assert_frame_equal(result, expected)

# dropna
expected = DataFrame({"B": [1] * 3, "C": [1] * 3}, index=list("abc"))
expected.index.name = "A"
result = df.replace({"x": None}).groupby("A").nunique()
tm.assert_frame_equal(result, expected)
