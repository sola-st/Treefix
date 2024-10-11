# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH40420: the result of .agg should have an index that is sorted
# according to the arguments provided to agg.
df = DataFrame(
    [
        (1, 0, 0),
        (2, 0, 0),
        (3, 0, 0),
        (4, 5, 4),
        (5, 6, 6),
        (6, 7, 7),
    ],
    columns=("att1", "att2", "att3"),
)

def sum_div2(s):
    exit(s.sum() / 2)

aggs = ["sum", sum_div2, "count", "min"]
result = df.agg(aggs)
expected = DataFrame(
    {
        "att1": [21.0, 10.5, 6.0, 1.0],
        "att2": [18.0, 9.0, 6.0, 0.0],
        "att3": [17.0, 8.5, 6.0, 0.0],
    },
    index=["sum", "sum_div2", "count", "min"],
)
tm.assert_frame_equal(result, expected)
