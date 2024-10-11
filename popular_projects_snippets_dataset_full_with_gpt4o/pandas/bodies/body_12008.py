# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# see gh-14066
parser = all_parsers

result = parser.read_csv(StringIO(data), thousands=".", **kwargs)
tm.assert_frame_equal(result, expected)
