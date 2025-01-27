# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# make sure that user-provided handles are not closed
parser = all_parsers

with open(datapath("io", "data", "csv", "iris.csv")) as path:

    reader = parser.read_csv(path, chunksize=1)
    assert not reader.handles.handle.closed
    try:
        with reader:
            next(reader)
            assert False
    except AssertionError:
        assert not reader.handles.handle.closed
