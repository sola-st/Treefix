# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# see gh-14983
parser = all_parsers
result = parser.read_csv(StringIO(data), header=None, **kwargs)
tm.assert_frame_equal(result, expected)
