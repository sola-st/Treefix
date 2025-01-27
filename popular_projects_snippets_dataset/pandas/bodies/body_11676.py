# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# see gh-7757
data = """a,b,c\n0,1,2\n1,2,3"""
parser = all_parsers

expected = DataFrame({"a": [0, 1], "b": [1, 2], "c": [2, 3]})
result = parser.read_csv(StringIO(data), header=[0])
tm.assert_frame_equal(result, expected)
