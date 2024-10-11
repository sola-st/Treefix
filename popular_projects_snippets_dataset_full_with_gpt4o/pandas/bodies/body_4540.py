# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#26825
arr = np.array(
    [
        [
            Timestamp("2013-01-01 00:00:00"),
            Timestamp("2013-01-02 00:00:00"),
            Timestamp("2013-01-03 00:00:00"),
        ],
        [
            Timestamp("2013-01-01 00:00:00-0500", tz="US/Eastern"),
            pd.NaT,
            Timestamp("2013-01-03 00:00:00-0500", tz="US/Eastern"),
        ],
        [
            Timestamp("2013-01-01 00:00:00+0100", tz="CET"),
            pd.NaT,
            Timestamp("2013-01-03 00:00:00+0100", tz="CET"),
        ],
    ],
    dtype=object,
).T
res = DataFrame(arr, columns=["A", "B", "C"])

expected_dtypes = [
    "datetime64[ns]",
    "datetime64[ns, US/Eastern]",
    "datetime64[ns, CET]",
]
assert (res.dtypes == expected_dtypes).all()
