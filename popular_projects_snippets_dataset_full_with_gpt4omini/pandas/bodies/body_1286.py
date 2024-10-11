# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
# invalid warning as we are returning a new object
# GH 8730
df1 = DataFrame({"x": Series(["a", "b", "c"]), "y": Series(["d", "e", "f"])})
df2 = df1[["x"]]

# this should not raise
df2["y"] = ["g", "h", "i"]
