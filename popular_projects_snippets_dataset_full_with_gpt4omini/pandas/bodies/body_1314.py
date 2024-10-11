# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# GH 20629
df = DataFrame(
    [[1, 2], [3, 4], [5, 6]], index=CategoricalIndex(["A", "B", "C"])
)

s = df[0]
assert s.loc["A"] == 1
assert s.at["A"] == 1

assert df.loc["B", 1] == 4
assert df.at["B", 1] == 4
