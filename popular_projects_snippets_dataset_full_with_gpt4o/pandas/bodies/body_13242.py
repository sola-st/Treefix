# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
# GH 20927
# when called as an iterator, only those chunks with a date > pd.Timestamp.max
# are returned as datetime.datetime, if this happens that whole chunk is returned
# as datetime.datetime
col_order = ["text", "dt_as_float", "dt_as_dt", "date_as_float", "date_as_date"]
fname = datapath("io", "sas", "data", "max_sas_date.sas7bdat")
results = []
for df in pd.read_sas(fname, encoding="iso-8859-1", chunksize=1):
    # SAS likes to left pad strings with spaces - lstrip before comparing
    df = df.applymap(lambda x: x.lstrip() if isinstance(x, str) else x)
    # GH 19732: Timestamps imported from sas will incur floating point errors
    try:
        df["dt_as_dt"] = df["dt_as_dt"].dt.round("us")
    except pd._libs.tslibs.np_datetime.OutOfBoundsDatetime:
        df = df.applymap(round_datetime_to_ms)
    except AttributeError:
        df["dt_as_dt"] = df["dt_as_dt"].apply(round_datetime_to_ms)
    df.reset_index(inplace=True, drop=True)
    results.append(df)
expected = [
    pd.DataFrame(
        {
            "text": ["max"],
            "dt_as_float": [253717747199.999],
            "dt_as_dt": [datetime(9999, 12, 29, 23, 59, 59, 999000)],
            "date_as_float": [2936547.0],
            "date_as_date": [datetime(9999, 12, 29)],
        },
        columns=col_order,
    ),
    pd.DataFrame(
        {
            "text": ["normal"],
            "dt_as_float": [1880323199.999],
            "dt_as_dt": [np.datetime64("2019-08-01 23:59:59.999")],
            "date_as_float": [21762.0],
            "date_as_date": [np.datetime64("2019-08-01")],
        },
        columns=col_order,
    ),
]
for result, expected in zip(results, expected):
    tm.assert_frame_equal(result, expected)
