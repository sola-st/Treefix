# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
# GH 20927
# NB. max datetime in SAS dataset is 31DEC9999:23:59:59.999
#    but this is read as 29DEC9999:23:59:59.998993 by a buggy
#    sas7bdat module
fname = datapath("io", "sas", "data", "max_sas_date.sas7bdat")
df = pd.read_sas(fname, encoding="iso-8859-1")

# SAS likes to left pad strings with spaces - lstrip before comparing
df = df.applymap(lambda x: x.lstrip() if isinstance(x, str) else x)
# GH 19732: Timestamps imported from sas will incur floating point errors
try:
    df["dt_as_dt"] = df["dt_as_dt"].dt.round("us")
except pd._libs.tslibs.np_datetime.OutOfBoundsDatetime:
    df = df.applymap(round_datetime_to_ms)
except AttributeError:
    df["dt_as_dt"] = df["dt_as_dt"].apply(round_datetime_to_ms)
# if there are any date/times > pandas.Timestamp.max then ALL in that chunk
# are returned as datetime.datetime
expected = pd.DataFrame(
    {
        "text": ["max", "normal"],
        "dt_as_float": [253717747199.999, 1880323199.999],
        "dt_as_dt": [
            datetime(9999, 12, 29, 23, 59, 59, 999000),
            datetime(2019, 8, 1, 23, 59, 59, 999000),
        ],
        "date_as_float": [2936547.0, 21762.0],
        "date_as_date": [datetime(9999, 12, 29), datetime(2019, 8, 1)],
    },
    columns=["text", "dt_as_float", "dt_as_dt", "date_as_float", "date_as_date"],
)
tm.assert_frame_equal(df, expected)
