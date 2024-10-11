# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# GH#42104
dti = DatetimeIndex(
    [
        "2018-12-31",
        "2019-03-31",
        "2019-06-30",
        "2019-09-30",
        "2019-12-31",
        "2020-03-31",
    ],
    freq="Q-DEC",
)
result = dti[::2].intersection(dti[1::2])
expected = dti[:0]
tm.assert_index_equal(result, expected)
