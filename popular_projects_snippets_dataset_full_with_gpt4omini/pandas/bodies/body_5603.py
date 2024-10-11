# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 15939

result = Series(
    Index(
        [
            Timestamp("20160101", tz="US/Eastern"),
            Timestamp("20160101", tz="US/Eastern"),
        ]
    )
).unique()
expected = DatetimeArray._from_sequence(
    np.array([Timestamp("2016-01-01 00:00:00-0500", tz="US/Eastern")])
)
tm.assert_extension_array_equal(result, expected)

result = Index(
    [
        Timestamp("20160101", tz="US/Eastern"),
        Timestamp("20160101", tz="US/Eastern"),
    ]
).unique()
expected = DatetimeIndex(
    ["2016-01-01 00:00:00"], dtype="datetime64[ns, US/Eastern]", freq=None
)
tm.assert_index_equal(result, expected)

result = pd.unique(
    Series(
        Index(
            [
                Timestamp("20160101", tz="US/Eastern"),
                Timestamp("20160101", tz="US/Eastern"),
            ]
        )
    )
)
expected = DatetimeArray._from_sequence(
    np.array([Timestamp("2016-01-01", tz="US/Eastern")])
)
tm.assert_extension_array_equal(result, expected)

result = pd.unique(
    Index(
        [
            Timestamp("20160101", tz="US/Eastern"),
            Timestamp("20160101", tz="US/Eastern"),
        ]
    )
)
expected = DatetimeIndex(
    ["2016-01-01 00:00:00"], dtype="datetime64[ns, US/Eastern]", freq=None
)
tm.assert_index_equal(result, expected)
