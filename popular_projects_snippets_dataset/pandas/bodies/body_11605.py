# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_empty.py
# see gh-12048
parser = all_parsers
result = parser.read_csv(StringIO("A,B"), dtype=str)

expected = DataFrame({"A": [], "B": []}, dtype=str)
tm.assert_frame_equal(result, expected)
