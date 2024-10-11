# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# gh-14418
#
# Don't close user provided file handles.
parser = c_parser_only

with open(csv1) as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        parser.read_csv(m)
        assert not m.closed
