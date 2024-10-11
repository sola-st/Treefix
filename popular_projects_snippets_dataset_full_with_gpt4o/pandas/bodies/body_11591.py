# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_mangle_dupes.py
parser = all_parsers

data = "a,a,b,b,b\n1,2,3,4,5"
result = parser.read_csv(StringIO(data), sep=",")

expected = DataFrame([[1, 2, 3, 4, 5]], columns=["a", "a.1", "b", "b.1", "b.2"])
tm.assert_frame_equal(result, expected)
