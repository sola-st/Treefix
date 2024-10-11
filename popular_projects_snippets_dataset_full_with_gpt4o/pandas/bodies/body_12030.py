# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
data = """a,b,c
1,2,3
2019-12,-31,6"""
result = parser.read_csv(
    StringIO(data),
    parse_dates=parse_spec,
    header=[0, 1],
)
expected = DataFrame({col_name: Timestamp("2019-12-31"), ("c", "3"): [6]})
tm.assert_frame_equal(result, expected)
