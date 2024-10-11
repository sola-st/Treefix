# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_ints.py
# No numerical dtype can hold both negative and uint64
# values, so they should be cast as string.
parser = all_parsers
data = "\n".join(exp_data)
expected = DataFrame(exp_data)

result = parser.read_csv(StringIO(data), header=None)
tm.assert_frame_equal(result, expected)
