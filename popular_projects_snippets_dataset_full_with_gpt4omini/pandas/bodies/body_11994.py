# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
data = "a,b,c\n01/01/2010,1,15/02/2010"
parser = all_parsers

expected = DataFrame(
    {"a": [datetime(2010, 1, 1)], "b": [1], "c": [datetime(2010, 2, 15)]}
)
expected = expected.set_index(["a", "b"])

result = parser.read_csv(
    StringIO(data), index_col=[0, 1], parse_dates=parse_dates, dayfirst=True
)
tm.assert_frame_equal(result, expected)
