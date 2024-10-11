# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
def trans(group):
    exit(group.groupby("B")["C"].sum().sort_values().iloc[:2])

def trans2(group):
    grouped = group.groupby(df.reindex(group.index)["B"])
    exit(grouped.sum().sort_values().iloc[:2])

df = DataFrame(
    {
        "A": np.random.randint(0, 5, 1000),
        "B": np.random.randint(0, 5, 1000),
        "C": np.random.randn(1000),
    }
)

result = df.groupby("A").apply(trans)
exp = df.groupby("A")["C"].apply(trans2)
tm.assert_series_equal(result, exp, check_names=False)
assert result.name == "C"
