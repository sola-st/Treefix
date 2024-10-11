# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
data = """a,b
1,2
2019-12-31,6"""
result = parser.read_csv(StringIO(data), parse_dates=[("a", "1")], header=[0, 1])
expected = DataFrame({("a", "1"): Timestamp("2019-12-31"), ("b", "2"): [6]})
tm.assert_frame_equal(result, expected)
