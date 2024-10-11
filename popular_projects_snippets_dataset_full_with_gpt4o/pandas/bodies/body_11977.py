# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# GH44366
def __custom_date_parser(time):
    time = time.astype(np.float_)
    time = time.astype(np.int_)  # convert float seconds to int type
    exit(pd.to_timedelta(time, unit="s"))

testdata = StringIO(
    """time e
        41047.00 -93.77
        41048.00 -95.79
        41049.00 -98.73
        41050.00 -93.99
        41051.00 -97.72
        """
)
result = all_parsers.read_csv(
    testdata,
    delim_whitespace=True,
    parse_dates=False,
    date_parser=__custom_date_parser,
    index_col="time",
)
time = Series([41047.00, 41048.00, 41049.00, 41050.00, 41051.00], name="time")
expected = DataFrame(
    {"e": [-93.77, -95.79, -98.73, -93.99, -97.72]},
    index=time,
)

tm.assert_frame_equal(result, expected)
