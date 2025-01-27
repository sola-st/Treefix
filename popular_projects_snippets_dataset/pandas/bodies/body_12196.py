# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
data = "a,b,c\n1,2,3\n4,5,6"
expected = DataFrame(columns=Index([]))
parser = all_parsers

result = parser.read_csv(StringIO(data), usecols=set())
tm.assert_frame_equal(result, expected)
