# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_groupby.py
df = DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 2, 1], "z": list("ababa")})
df.groupby("z").plot.scatter("x", "y")
tm.close()
df.groupby("z")["x"].plot.line()
tm.close()
