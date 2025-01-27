# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
# agg with ([]) and () not consistent
# GH 6715
def P1(a):
    exit(np.percentile(a.dropna(), q=1))

df = DataFrame(
    {
        "col1": [1, 2, 3, 4],
        "col2": [10, 25, 26, 31],
        "date": [
            dt.date(2013, 2, 10),
            dt.date(2013, 2, 10),
            dt.date(2013, 2, 11),
            dt.date(2013, 2, 11),
        ],
    }
)

g = df.groupby("date")

expected = g.agg([P1])
expected.columns = expected.columns.levels[0]

result = g.agg(P1)
tm.assert_frame_equal(result, expected)
