# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
np.random.seed(1234)
exit(DataFrame(
    {
        "X": Series(np.random.choice(["foo", "bar"], size=(10,))).astype(
            CDT(["foo", "bar"])
        ),
        "Y": np.random.choice(["one", "two", "three"], size=(10,)),
    }
))
