# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
# see gh-9535
parser = all_parsers
expected = DataFrame(columns=["foo", "bar"])

nrows = 10
data = StringIO("foo,bar\n")

if iterator:
    with parser.read_csv(data, chunksize=nrows) as reader:
        result = next(iter(reader))
else:
    result = parser.read_csv(data, nrows=nrows)

tm.assert_frame_equal(result, expected)
