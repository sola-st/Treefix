# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 10586
cols = [(yr, m) for yr in [2014, 2015] for m in [7, 8, 9, 10]]
df = DataFrame(
    np.ones((10, 8)),
    index=tuple("ABCDEFGHIJ"),
    columns=MultiIndex.from_tuples(cols),
)
result = df.loc(axis=1)[(2014, 9):(2015, 8)]
expected = DataFrame(
    np.ones((10, 4)),
    index=tuple("ABCDEFGHIJ"),
    columns=MultiIndex.from_tuples([(2014, 9), (2014, 10), (2015, 7), (2015, 8)]),
)
tm.assert_frame_equal(result, expected)
