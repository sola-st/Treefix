# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_skiprows.py
# see gh-12775 and gh-10911
parser = all_parsers
result = parser.read_csv(StringIO(data), **kwargs)
tm.assert_frame_equal(result, expected)
