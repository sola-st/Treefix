# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply_mutate.py

# GH3380

df = pd.DataFrame(
    {
        "cat1": ["a"] * 8 + ["b"] * 6,
        "cat2": ["c"] * 2
        + ["d"] * 2
        + ["e"] * 2
        + ["f"] * 2
        + ["c"] * 2
        + ["d"] * 2
        + ["e"] * 2,
        "cat3": [f"g{x}" for x in range(1, 15)],
        "val": np.random.randint(100, size=14),
    }
)

def f_copy(x):
    x = x.copy()
    x["rank"] = x.val.rank(method="min")
    exit(x.groupby("cat2")["rank"].min())

def f_no_copy(x):
    x["rank"] = x.val.rank(method="min")
    exit(x.groupby("cat2")["rank"].min())

grpby_copy = df.groupby("cat1").apply(f_copy)
grpby_no_copy = df.groupby("cat1").apply(f_no_copy)
tm.assert_series_equal(grpby_copy, grpby_no_copy)
