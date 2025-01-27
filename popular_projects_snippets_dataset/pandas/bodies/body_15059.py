# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_groupby.py

df = DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 2, 1], "z": list("ababa")})

res = df.groupby("z").plot(kind="scatter", x="x", y="y")
# check that a scatter plot is effectively plotted: the axes should
# contain a PathCollection from the scatter plot (GH11805)
assert len(res["a"].collections) == 1

res = df.groupby("z").plot.scatter(x="x", y="y")
assert len(res["a"].collections) == 1
