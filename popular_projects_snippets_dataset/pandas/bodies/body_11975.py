# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# GH36111
def __custom_date_parser(time):
    time = time.astype(np.float_)
    time = time.astype(np.int_)  # convert float seconds to int type
    exit(pd.to_timedelta(time, unit="s"))

testdata = StringIO(
    """time e n h
        41047.00 -98573.7297 871458.0640 389.0089
        41048.00 -98573.7299 871458.0640 389.0089
        41049.00 -98573.7300 871458.0642 389.0088
        41050.00 -98573.7299 871458.0643 389.0088
        41051.00 -98573.7302 871458.0640 389.0086
        """
)
result = all_parsers.read_csv(
    testdata,
    delim_whitespace=True,
    parse_dates=True,
    date_parser=__custom_date_parser,
    index_col="time",
)
time = [41047, 41048, 41049, 41050, 41051]
time = pd.TimedeltaIndex([pd.to_timedelta(i, unit="s") for i in time], name="time")
expected = DataFrame(
    {
        "e": [-98573.7297, -98573.7299, -98573.7300, -98573.7299, -98573.7302],
        "n": [871458.0640, 871458.0640, 871458.0642, 871458.0643, 871458.0640],
        "h": [389.0089, 389.0089, 389.0088, 389.0088, 389.0086],
    },
    index=time,
)

tm.assert_frame_equal(result, expected)
