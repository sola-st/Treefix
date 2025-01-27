# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_index.py
# see gh-14545
parser = all_parsers
data = expected.to_csv(index=False) if round_trip else data

result = parser.read_csv(StringIO(data), header=header)
tm.assert_frame_equal(result, expected)
