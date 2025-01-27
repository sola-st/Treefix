# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
# see gh-6710
data = "1,2\n1,2,3"
parser = all_parsers
names = ["a", "b", "c"]
expected = DataFrame({"a": [1, 1], "c": [np.nan, 3]})

result = parser.read_csv(StringIO(data), names=names, usecols=usecols)
tm.assert_frame_equal(result, expected)
