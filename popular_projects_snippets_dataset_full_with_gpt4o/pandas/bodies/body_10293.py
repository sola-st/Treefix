# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_size.py
df = DataFrame([[1, 1], [2, 2]], columns=["A", "B"])
df["A"] = df["A"].astype("category")
result = df.groupby(["A", "B"], as_index=as_index).size()

expected = DataFrame(
    [[1, 1, 1], [1, 2, 0], [2, 1, 0], [2, 2, 1]], columns=["A", "B", "size"]
)
expected["A"] = expected["A"].astype("category")
if as_index:
    expected = expected.set_index(["A", "B"])["size"].rename(None)

tm.assert_equal(result, expected)
