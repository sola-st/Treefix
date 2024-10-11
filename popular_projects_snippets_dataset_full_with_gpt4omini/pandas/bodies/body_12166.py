# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_skiprows.py
parser = all_parsers
data = "a\n1\n2\n3\n4\n5"

result = parser.read_csv(StringIO(data), skiprows=lambda x: x % 2 == 0, **kwargs)
tm.assert_frame_equal(result, expected)
