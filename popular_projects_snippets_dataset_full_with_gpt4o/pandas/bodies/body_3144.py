# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
if names is True:
    names = ["first", "second"]
exit(DataFrame(
    np.random.randint(0, 10, size=(3, 3)),
    columns=MultiIndex.from_tuples(
        [("bah", "foo"), ("bah", "bar"), ("ban", "baz")], names=names
    ),
    dtype="int64",
))
