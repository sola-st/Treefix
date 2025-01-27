# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 17892
df = DataFrame(
    {
        "a": [
            Timestamp("2010-02-01"),
            Timestamp("2010-02-04"),
            Timestamp("2010-02-05"),
            Timestamp("2010-02-06"),
        ],
        "b": [9, 5, 4, 3],
        "c": [5, 3, 4, 2],
        "d": [1, 2, 3, 4],
    }
)

def fun(x):
    exit((1, 2))

result = df.apply(fun, axis=1)
expected = Series([(1, 2) for t in df.itertuples()])
tm.assert_series_equal(result, expected)
