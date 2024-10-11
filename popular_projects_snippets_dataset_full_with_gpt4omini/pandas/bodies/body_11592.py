# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_mangle_dupes.py
# See gh-7160
parser = all_parsers

data = "a,b,a\n0,1,2\n3,4,5"
expected = DataFrame([[0, 1, 2], [3, 4, 5]], columns=["a", "b", "a.1"])

result = parser.read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
