# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
parser = all_parsers
data = "a  b  c\n4  apple  bat  5.7\n8  orange  cow  10"

result = parser.read_csv(StringIO(data), delim_whitespace=True, usecols=("a", "b"))
expected = DataFrame({"a": ["apple", "orange"], "b": ["bat", "cow"]}, index=[4, 8])
tm.assert_frame_equal(result, expected)
