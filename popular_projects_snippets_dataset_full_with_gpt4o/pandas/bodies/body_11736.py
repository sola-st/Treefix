# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_ints.py
# see gh-2601
data = "65248E10 11\n55555E55 22\n"
parser = all_parsers

result = parser.read_csv(StringIO(data), header=None, sep=sep)
expected = DataFrame([[6.5248e14, 11], [5.5555e59, 22]])
tm.assert_frame_equal(result, expected)
