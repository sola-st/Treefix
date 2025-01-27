# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
data = """A,B,C
20090101,a,1,2
20090102,b,3,4
20090103,c,4,5
"""
parser = all_parsers
result = parser.read_csv(
    StringIO(data), date_parser=lambda x: datetime.strptime(x, "%Y%m%d")
)
expected = parser.read_csv(StringIO(data), parse_dates=True)
tm.assert_frame_equal(result, expected)
