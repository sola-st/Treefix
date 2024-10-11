# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# segfault in GH#3308
d = {"t1": [2, 2.5, 3], "t2": [4, 5, 6]}
df = DataFrame(d)
tuples = [(0, 1), (0, 2), (1, 2)]
df["tuples"] = tuples

index = MultiIndex.from_tuples(df["tuples"])
# it works!
df.set_index(index)
