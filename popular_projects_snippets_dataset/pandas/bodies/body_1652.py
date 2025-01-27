# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
B = np.concatenate((np.arange(1000), np.arange(1000), np.arange(500)))
A = np.arange(2500)
df = DataFrame(
    {
        "A": A,
        "B": B,
        "C": A,
        "D": B,
        "E": A,
        "F": B,
        "G": A,
        "H": B,
        "values": np.random.randn(2500),
    }
)

lg = df.groupby(["A", "B", "C", "D", "E", "F", "G", "H"])
rg = df.groupby(["H", "G", "F", "E", "D", "C", "B", "A"])

left = lg.sum()["values"]
right = rg.sum()["values"]

exp_index, _ = left.index.sortlevel()
tm.assert_index_equal(left.index, exp_index)

exp_index, _ = right.index.sortlevel(0)
tm.assert_index_equal(right.index, exp_index)

tups = list(map(tuple, df[["A", "B", "C", "D", "E", "F", "G", "H"]].values))
tups = com.asarray_tuplesafe(tups)

expected = df.groupby(tups).sum()["values"]

for k, v in expected.items():
    assert left[k] == right[k[::-1]]
    assert left[k] == v
assert len(left) == len(right)
