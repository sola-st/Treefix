# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
# see gh-7630
data1 = pd.to_datetime("20100101 01:01").tz_localize("UTC")
df1 = DataFrame(
    columns=["UTCdatetime", "abc"],
    data=data1,
    index=pd.date_range("20140627", periods=1),
)
data2 = pd.to_datetime("20121212 12:12").tz_localize("UTC")
df2 = DataFrame(
    columns=["UTCdatetime", "xyz"],
    data=data2,
    index=pd.date_range("20140628", periods=1),
)
res = df2[["UTCdatetime"]].combine_first(df1)
exp = DataFrame(
    {
        "UTCdatetime": [
            pd.Timestamp("2010-01-01 01:01", tz="UTC"),
            pd.Timestamp("2012-12-12 12:12", tz="UTC"),
        ],
        "abc": [pd.Timestamp("2010-01-01 01:01:00", tz="UTC"), pd.NaT],
    },
    columns=["UTCdatetime", "abc"],
    index=pd.date_range("20140627", periods=2, freq="D"),
)
assert res["UTCdatetime"].dtype == "datetime64[ns, UTC]"
assert res["abc"].dtype == "datetime64[ns, UTC]"

tm.assert_frame_equal(res, exp)

# see gh-10567
dts1 = pd.date_range("2015-01-01", "2015-01-05", tz="UTC")
df1 = DataFrame({"DATE": dts1})
dts2 = pd.date_range("2015-01-03", "2015-01-05", tz="UTC")
df2 = DataFrame({"DATE": dts2})

res = df1.combine_first(df2)
tm.assert_frame_equal(res, df1)
assert res["DATE"].dtype == "datetime64[ns, UTC]"

dts1 = pd.DatetimeIndex(
    ["2011-01-01", "NaT", "2011-01-03", "2011-01-04"], tz="US/Eastern"
)
df1 = DataFrame({"DATE": dts1}, index=[1, 3, 5, 7])
dts2 = pd.DatetimeIndex(
    ["2012-01-01", "2012-01-02", "2012-01-03"], tz="US/Eastern"
)
df2 = DataFrame({"DATE": dts2}, index=[2, 4, 5])

res = df1.combine_first(df2)
exp_dts = pd.DatetimeIndex(
    [
        "2011-01-01",
        "2012-01-01",
        "NaT",
        "2012-01-02",
        "2011-01-03",
        "2011-01-04",
    ],
    tz="US/Eastern",
)
exp = DataFrame({"DATE": exp_dts}, index=[1, 2, 3, 4, 5, 7])
tm.assert_frame_equal(res, exp)

# different tz
dts1 = pd.date_range("2015-01-01", "2015-01-05", tz="US/Eastern")
df1 = DataFrame({"DATE": dts1})
dts2 = pd.date_range("2015-01-03", "2015-01-05")
df2 = DataFrame({"DATE": dts2})

# if df1 doesn't have NaN, keep its dtype
res = df1.combine_first(df2)
tm.assert_frame_equal(res, df1)
assert res["DATE"].dtype == "datetime64[ns, US/Eastern]"

dts1 = pd.date_range("2015-01-01", "2015-01-02", tz="US/Eastern")
df1 = DataFrame({"DATE": dts1})
dts2 = pd.date_range("2015-01-01", "2015-01-03")
df2 = DataFrame({"DATE": dts2})

res = df1.combine_first(df2)
exp_dts = [
    pd.Timestamp("2015-01-01", tz="US/Eastern"),
    pd.Timestamp("2015-01-02", tz="US/Eastern"),
    pd.Timestamp("2015-01-03"),
]
exp = DataFrame({"DATE": exp_dts})
tm.assert_frame_equal(res, exp)
assert res["DATE"].dtype == "object"
