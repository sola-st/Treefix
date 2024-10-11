# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
data = """foo,bar,baz
31/01/2010,1,2
01/02/2010,1,NA
02/02/2010,1,2
"""
if "dayfirst" in kwargs:
    df = parser.read_csv(
        StringIO(data),
        names=["time", "Q", "NTU"],
        date_parser=lambda d: du_parse(d, **kwargs),
        header=0,
        index_col=0,
        parse_dates=True,
        na_values=["NA"],
    )
    exp_index = Index(
        [datetime(2010, 1, 31), datetime(2010, 2, 1), datetime(2010, 2, 2)],
        name="time",
    )
    expected = DataFrame(
        {"Q": [1, 1, 1], "NTU": [2, np.nan, 2]},
        index=exp_index,
        columns=["Q", "NTU"],
    )
    tm.assert_frame_equal(df, expected)
else:
    msg = "got an unexpected keyword argument 'day_first'"
    with pytest.raises(TypeError, match=msg):
        parser.read_csv(
            StringIO(data),
            names=["time", "Q", "NTU"],
            date_parser=lambda d: du_parse(d, **kwargs),
            skiprows=[0],
            index_col=0,
            parse_dates=True,
            na_values=["NA"],
        )
