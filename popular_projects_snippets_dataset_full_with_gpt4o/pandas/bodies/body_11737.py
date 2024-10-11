# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_ints.py
# see gh-2599
parser = all_parsers
data = "A,B\n0,0\n0,"
result = parser.read_csv(StringIO(data))

expected = DataFrame({"A": [0, 0], "B": [0, np.nan]})
tm.assert_frame_equal(result, expected)
