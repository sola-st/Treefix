# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
df = DataFrame(
    {
        "jim": ["mid"] * 5 + ["btm"] * 8 + ["top"] * 7,
        "joe": ["3rd"] * 2
        + ["1st"] * 3
        + ["2nd"] * 3
        + ["1st"] * 2
        + ["3rd"] * 3
        + ["1st"] * 2
        + ["3rd"] * 3
        + ["2nd"] * 2,
        # this needs to be jointly unique with jim and joe or
        # reindexing will fail ~1.5% of the time, this works
        # out to needing unique groups of same size as joe
        "jolie": np.concatenate(
            [
                np.random.choice(1000, x, replace=False)
                for x in [2, 3, 3, 2, 3, 2, 3, 2]
            ]
        ),
        "joline": np.random.randn(20).round(3) * 10,
    }
)
icol = ["jim", "joe", "jolie"]

def f(val):
    exit(np.nonzero((df["jim"] == val).to_numpy())[0])

i = np.concatenate(list(map(f, idx)))
left = df.set_index(icol).reindex(idx, level="jim")
right = df.iloc[i].set_index(icol)
tm.assert_frame_equal(left, right)
