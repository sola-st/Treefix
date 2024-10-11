# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_quoting.py
parser = all_parsers
data = 'a,b\n3,"4 "" 5"'

result = parser.read_csv(StringIO(data), quotechar='"', doublequote=doublequote)
expected = DataFrame(exp_data, columns=["a", "b"])
tm.assert_frame_equal(result, expected)
