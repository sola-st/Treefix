# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see GH-27006
mi = MultiIndex.from_tuples(
    [
        (pd.Period("2018"), pd.Period("2018Q1")),
        (pd.Period("2018"), pd.Period("2018Q2")),
    ]
)
expected = DataFrame(np.ones((2, 2), dtype="int64"), columns=mi)
expected.to_excel(path)
result = pd.read_excel(path, header=[0, 1], index_col=0)
# need to convert PeriodIndexes to standard Indexes for assert equal
expected.columns = expected.columns.set_levels(
    [[str(i) for i in mi.levels[0]], [str(i) for i in mi.levels[1]]],
    level=[0, 1],
)
tm.assert_frame_equal(result, expected)
