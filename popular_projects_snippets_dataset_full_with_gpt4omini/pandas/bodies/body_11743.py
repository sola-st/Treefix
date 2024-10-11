# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_index.py
parser = all_parsers
result = parser.read_csv(StringIO(data), **kwargs)
tm.assert_frame_equal(result, expected)
