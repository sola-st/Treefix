# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_put.py
exit(MultiIndex.from_tuples(
    [
        (datetime.datetime(2013, 12, d), s, t)
        for d in range(1, 3)
        for s in range(2)
        for t in range(3)
    ],
    names=names,
))
