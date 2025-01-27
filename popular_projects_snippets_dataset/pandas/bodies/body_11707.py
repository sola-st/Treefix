# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# gh-14418
#
# Don't close user provided file handles.
parser = all_parsers
data = "a,b\n1,2"

fh = StringIO(data)
parser.read_csv(fh)
assert not fh.closed
