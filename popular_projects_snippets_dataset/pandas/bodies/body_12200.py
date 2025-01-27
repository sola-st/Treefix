# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
# see gh-8985
parser = all_parsers
result = parser.read_csv(StringIO(data), usecols=usecols, **kwargs)
tm.assert_frame_equal(result, expected)
