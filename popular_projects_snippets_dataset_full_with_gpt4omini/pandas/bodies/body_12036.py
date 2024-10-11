# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# GH#26203
parser = all_parsers
data = """Test
2012-10-01
0
2015-05-15
#
2017-09-09
"""
result = parser.read_csv(
    StringIO(data),
    na_values={"Test": ["#", "0"]},
    parse_dates=["Test"],
    date_parser=lambda x: pd.to_datetime(x, format="%Y-%m-%d"),
)
expected = DataFrame(
    {
        "Test": [
            Timestamp("2012-10-01"),
            pd.NaT,
            Timestamp("2015-05-15"),
            pd.NaT,
            Timestamp("2017-09-09"),
        ]
    }
)
tm.assert_frame_equal(result, expected)
