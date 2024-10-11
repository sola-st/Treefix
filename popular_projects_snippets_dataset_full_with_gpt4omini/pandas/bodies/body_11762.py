# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
# see gh-23509
parser = all_parsers
data = "\n".join(["0"] * 7 + [",".join(["0"] * 10)])

expected = DataFrame([[0] + [np.nan] * 9] * 7 + [[0] * 10])
with parser.read_csv(StringIO(data), names=range(10), chunksize=4) as reader:
    result = concat(reader)
tm.assert_frame_equal(result, expected)
