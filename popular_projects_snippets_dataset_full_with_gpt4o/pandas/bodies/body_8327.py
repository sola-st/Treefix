# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# GH#38196
idx1 = Index(
    [
        pd.Timestamp("2019-12-13"),
        pd.Timestamp("2019-12-12"),
        pd.Timestamp("2019-12-12"),
    ]
)
result = idx1.intersection(idx1, sort=sort)
expected = Index([pd.Timestamp("2019-12-13"), pd.Timestamp("2019-12-12")])
tm.assert_index_equal(result, expected)
