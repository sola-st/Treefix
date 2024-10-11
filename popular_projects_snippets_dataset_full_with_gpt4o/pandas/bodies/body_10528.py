# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_cython.py
# #2113
df = DataFrame({"x": [1, 2, 3], "y": [3, 4, 5]})

df.groupby(level=0, axis="columns").mean()
df.groupby(level=0, axis="columns").mean()
df.groupby(level=0, axis="columns").mean()
df.groupby(level=0, axis="columns").mean()
