# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# make sure that opened files are closed
parser = all_parsers

path = datapath("io", "data", "csv", "iris.csv")

reader = parser.read_csv(path, chunksize=1)
assert not reader.handles.handle.closed
try:
    with reader:
        next(reader)
        assert False
except AssertionError:
    assert reader.handles.handle.closed
